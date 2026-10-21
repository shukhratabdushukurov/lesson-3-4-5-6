from tg_bot.loader import bot
from telebot import types
from tg_bot.keyboards import reply
from tg_bot.states import CategoryStates
from telebot.states.sync import StateContext
from database.managers.base import BaseManager

db_manager = BaseManager()

@bot.message_handler(is_admin=True, commands=['start'])
def admin_start(message: types.Message):
    bot.send_message(message.chat.id, 'Здравствуйте, Администратор', reply_markup=reply.admin_kb())



@bot.message_handler(is_admin=True, func=lambda message: message.text == 'Категории')
def handle_categories(message: types.Message, state: StateContext):
    state.set(CategoryStates.start)
    bot.send_message(message.chat.id, 'Выберите действие над категориями', reply_markup=reply.admin_actions_kb())

@bot.message_handler(is_admin=True, func=lambda message: message.text == 'Добавить', state=CategoryStates.start)
def add_category(message: types.Message, state: StateContext):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Введите название категории')
    state.set(CategoryStates.name)

@bot.message_handler(is_admin=True, state=CategoryStates.name)
def insert_category(message: types.Message, state: StateContext):
    chat_id = message.chat.id
    db_manager.manage('INSERT INTO categories(name) values (%s)', message.text, commit=True)
    bot.send_message(chat_id, f'Категория: "{message.text}" создана')
    state.delete()

@bot.message_handler(is_admin=True, func=lambda message: message.text == 'Просмотреть', state=CategoryStates.start)
def show_category(message: types.Message, state: StateContext):
    chat_id = message.chat.id
    db_manager.manage('SELECT * FROM CATEGORIES;', commit=True)
    state.set(CategoryStates.name)
    for i in db_manager:

    bot.send_message(chat_id, f'Категория: "{message.text}" создана')


    db_manager.manage('SELECT * FROM categories;', commit=True)




@bot.message_handler(is_admin=True, func=lambda message: message.text == 'Продукты')
def handle_products(message: types.Message):
    bot.send_message(message.chat.id, 'Выберите действие над продуктами', reply_markup=reply.admin_actions_kb())




@bot.message_handler(is_admin=True, func=lambda message: message.text == 'Пользователи')
def handle_users(message: types.Message):
    bot.send_message(message.chat.id, 'Выберите действие над пользователями', reply_markup=reply.admin_actions_kb())
