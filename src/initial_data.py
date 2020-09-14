import datetime
from collections import namedtuple
from datetime import date

from api.mwe import add_mwe
from bot.helpers.time_helper import get_time_in_turkey
from i18n import Language
from models import MweCategory

mwe = namedtuple("mwe", ["name", "description", "lemmas", "category"])

turkish_mwes = [
        mwe("ortaya çıkmak", "yokken var olmak, meydana çıkmak, türemek",
            ["orta", "çık"], MweCategory.VID),
        mwe("ayvayı yemek", "kötü bir duruma düşmek", ["ayva", "ye"],
            MweCategory.VID),
        mwe("yer almak", "bir işi hazırlayanlar arasında bulunmak.",
            ["yer", "al"], MweCategory.VID),
        mwe("dikkat çekmek", "ilgi toplamak, göze batmak, fark edilmek.",
            ["dikkat", "çek"], MweCategory.VID)
]

english_mwes = [
        mwe("(to) give up", "cease making an effort; admit defeat",
            ["give", "up"], MweCategory.VPC),
        mwe("let (someone) know", "to give information to (someone)",
            ["let", "know"], MweCategory.VPC)
]

turkey_time = get_time_in_turkey()
mwe_date = date(turkey_time.year, turkey_time.month, turkey_time.day)
for mwe in turkish_mwes:
    add_mwe(mwe.name, mwe.description, Language.TURKISH, mwe_date, mwe.lemmas,
            mwe.category)
    mwe_date += datetime.timedelta(days=1)

mwe_date = date(turkey_time.year, turkey_time.month, turkey_time.day)
for mwe in english_mwes:
    add_mwe(mwe.name, mwe.description, Language.ENGLISH, mwe_date, mwe.lemmas,
            mwe.category)
    mwe_date += datetime.timedelta(days=1)
