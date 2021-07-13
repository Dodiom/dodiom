from bot.main import mwexpress_bot
from log import mwelog
from cron import schedule_jobs, run_scheduled_jobs
from initial_data import load_initial_data

load_initial_data()

mwelog.info("Starting MWExpress...")

mwexpress_bot.listen()

schedule_jobs()
run_scheduled_jobs()
