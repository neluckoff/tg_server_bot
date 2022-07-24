from server import Server
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN, ADMIN_ID

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer(connect.command(message.text))
    else:
        await message.answer('Only the owner of the bot can write commands!')


async def on_startup(_):
    await bot.send_message(chat_id=ADMIN_ID, text=connect.start_message())


if __name__ == '__main__':
    connect = Server()
    connect.start()
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
