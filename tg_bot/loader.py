from telebot import TeleBot
import telebot
import betterlogging as logging

from settings.loader import settings
from .filters import IsAdmin

logging.basic_colorized_config(level=logging.DEBUG)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

bot = TeleBot(settings.bot.token, parse_mode='HTML')
bot.add_custom_filter(IsAdmin())