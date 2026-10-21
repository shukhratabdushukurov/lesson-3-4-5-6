from telebot import custom_filters
from settings.loader import settings


class IsAdmin(custom_filters.SimpleCustomFilter):
    key = 'is_admin'

    @staticmethod
    def check(message):
        return message.from_user.id in settings.bot.admin_ids

