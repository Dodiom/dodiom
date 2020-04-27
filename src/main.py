import logging

from database import init_database
from bot.main import updater

from log import init_seqlog

init_seqlog()

logging.info("Starting MWExpress...")

init_database()

logging.info("Listening Telegram for connections...")
updater.start_polling()
updater.idle()
