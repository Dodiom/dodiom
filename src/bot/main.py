import logging
from telegram.ext import Updater

from bot.handlers.message import message_handler, sticker_handler
from bot.handlers.start import start_handler
from config import mwexpress_config


class MWExpress:
    def __init__(self):
        self.updater = Updater(mwexpress_config.telegram_api_key, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.bot = self.dispatcher.bot

        self.dispatcher.add_handler(start_handler)
        self.dispatcher.add_handler(message_handler)
        self.dispatcher.add_handler(sticker_handler)

    def listen(self):
        logging.info("Listening Telegram for connections...")
        self.updater.start_polling()
        # self.updater.idle()


mwexpress_bot = MWExpress()
