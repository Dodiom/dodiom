from telegram.ext import Updater, Dispatcher

from bot.handlers.announcements import announcements_handler, review_happy_hour_handler, i_need_x_examples_handler
from bot.handlers.message import message_handler, sticker_handler
from bot.handlers.start import start_handler
from bot.handlers.stats import stats_handler
from config import mwexpress_config
from log import mwelog


class MWExpress:
    def __init__(self):
        self.updater = Updater(mwexpress_config.telegram_api_key, use_context=True, workers=8)
        self.dispatcher: Dispatcher = self.updater.dispatcher
        self.bot = self.dispatcher.bot

        self.dispatcher.add_handler(start_handler)
        self.dispatcher.add_handler(announcements_handler)
        self.dispatcher.add_handler(review_happy_hour_handler)
        self.dispatcher.add_handler(i_need_x_examples_handler)
        self.dispatcher.add_handler(stats_handler)
        self.dispatcher.add_handler(message_handler)
        self.dispatcher.add_handler(sticker_handler)

    def listen(self):
        mwelog.info("Listening Telegram for connections...")
        self.updater.start_polling()
        # self.updater.idle()


mwexpress_bot = MWExpress()
