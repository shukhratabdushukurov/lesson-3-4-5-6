from telebot import types

def admin_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(
        types.KeyboardButton('Категории'),
        types.KeyboardButton('Продукты'),
        types.KeyboardButton('Пользователи'),
    )
    return kb

def admin_actions_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(
        types.KeyboardButton('Добавить'),
        types.KeyboardButton('Просмотреть'),
    )
    return kb