import logging

from bot.main import mwexpress_bot
from test_data import load_test_data
from log import init_seqlog
from cron import schedule_jobs, run_scheduled_jobs

init_seqlog()

logging.info("Starting MWExpress...")

# load_test_data()

mwexpress_bot.listen()

schedule_jobs()
run_scheduled_jobs()
