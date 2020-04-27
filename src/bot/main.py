import os
from telegram.ext import Updater

from bot.handlers.message import message_handler
from bot.handlers.start import start_handler

updater = Updater(os.environ["TELEGRAM_API_KEY"], use_context=True)
dispatcher = updater.dispatcher
bot = dispatcher.bot


dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)