import pytz
from datetime import datetime


def get_time_in_turkey() -> datetime:
    turkey_time = pytz.timezone('Europe/Istanbul')
    return datetime.now(turkey_time)
