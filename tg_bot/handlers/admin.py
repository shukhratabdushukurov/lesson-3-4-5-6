from tg_bot.loader import bot
from telebot import types
@bot.message_handler(is_admin=True, commands=['start'])
def admin_start(message: types.Message):
    bot.send_message(message.chat.id, 'Здравствуйте, Администратор')