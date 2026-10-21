from tg_bot.loader import bot
from telebot import types

@bot.message_handler(is_admin=False, commands=['start'])
def start(message: types.Message):
    chat_id = message.chat.id

    bot.send_message(chat_id, 'Hello Hello')