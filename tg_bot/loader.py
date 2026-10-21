from telebot import TeleBot
import telebot
import betterlogging as logging

from settings.loader import settings
from .filters import IsAdmin

from telebot.states.sync import StateMiddleware
from telebot.custom_filters import StateFilter
from telebot.storage import StateMemoryStorage


logging.basic_colorized_config(level=logging.DEBUG)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

bot = TeleBot(settings.bot.token, parse_mode='HTML',
              state_storage=StateMemoryStorage(), use_class_middlewares=True)
bot.add_custom_filter(IsAdmin())
bot.add_custom_filter(StateFilter(bot))
bot.setup_middleware((StateMiddleware(bot)))