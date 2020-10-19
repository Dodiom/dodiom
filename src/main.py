from bot.main import mwexpress_bot
from log import init_seqlog, mwelog
from cron import schedule_jobs, run_scheduled_jobs

init_seqlog()

mwelog.info("Starting MWExpress...")

mwexpress_bot.listen()

schedule_jobs()
run_scheduled_jobs()
