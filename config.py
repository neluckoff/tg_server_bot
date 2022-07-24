from environs import Env

env = Env()
env.read_env()

hostname = env.str("host")
port = env.int("port")
username = env.str("user")
password = env.str("pass")

TOKEN = env.str("API_TOKEN")
ADMIN_ID = env.int("ADMIN_ID")
