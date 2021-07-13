import datetime
from json import loads
from datetime import datetime

from api.mwe import get_date_mwe, add_mwe
from config import mwexpress_config
from models import MweCategory
from log import mwelog


def load_initial_data():
    with open("idioms.json", encoding="utf-8") as initial_idioms_file:
        initial_idioms = loads(initial_idioms_file.read())
        for i in range(len(initial_idioms)):
            initial_idioms[i]['day'] = datetime.fromisoformat(initial_idioms[i]['day']).date()
            if initial_idioms[i]['category'] == 'VID':
                initial_idioms[i]['category'] = MweCategory.VID
            elif initial_idioms[i]['category'] == 'VPC':
                initial_idioms[i]['category'] = MweCategory.VPC
            else:
                raise ValueError(f'Category cannot be {initial_idioms[i]["category"]}')

        for initial_mwe in initial_idioms:
            mwe = get_date_mwe(mwexpress_config.language, initial_mwe['day'])
            if mwe is None:
                add_mwe(initial_mwe['name'],
                        initial_mwe['meaning'],
                        mwexpress_config.language,
                        initial_mwe['day'],
                        initial_mwe['lemmas'],
                        initial_mwe['category'])
                mwelog.info(f'Added mwe: {initial_mwe["name"]}')
