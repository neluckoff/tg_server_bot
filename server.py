import time
import paramiko
from config import hostname, port, username, password


class Server:
    def __init__(self):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.sleep_time = 2
        self.channel = None
        self.client = None

    def start(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=self.hostname, port=self.port,
                            username=self.username, password=self.password, compress=True)
        self.channel = self.client.invoke_shell()

    def start_message(self):
        self.channel.send('\n')
        stdout = self.channel.recv(1024)
        return str(stdout.decode())

    def command(self, msg):
        self.channel.send(msg + '\n')
        time.sleep(self.sleep_time)
        stdout = self.channel.recv(1024)
        text = str(stdout.decode())
        text = '\n'.join(text.split('\n')[1:])
        return text

    def command_sudo(self, msg):
        self.channel.send(msg + '\n')
        self.channel.send(self.password + '\n')
        time.sleep(self.sleep_time)
        stdout = self.channel.recv(1024)
        text = str(stdout.decode())
        text = '\n'.join(text.split('\n')[1:])
        return text
