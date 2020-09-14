import logging
import os
from telegram.ext import Updater

from bot.handlers.message import message_handler
from bot.handlers.start import start_handler


class MWExpress:
    def __init__(self):
        self.updater = Updater(os.environ["TELEGRAM_API_KEY"], use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.bot = self.dispatcher.bot

        self.dispatcher.add_handler(start_handler)
        self.dispatcher.add_handler(message_handler)

    def listen(self):
        logging.info("Listening Telegram for connections...")
        self.updater.start_polling()
        # self.updater.idle()


mwexpress_bot = MWExpress()
