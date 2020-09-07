import logging

from bot.main import MWExpress
from test_data import load_test_data
from log import init_seqlog

init_seqlog()

logging.info("Starting MWExpress...")

# load_test_data()

bot = MWExpress()
bot.listen()
