from settings.loader import settings
from tg_bot.loader import bot
from tg_bot.handlers import user
from tg_bot.handlers import admin
from database.managers.base import table_manager


def main():
    table_manager.create_tables()
    print(table_manager.manage('SELECT * FROM categories;', fetchall=True))
    bot.infinity_polling()


main()
