import datetime
from collections import namedtuple
from datetime import date

from api.mwe import add_mwe
from i18n import Language
from models import MweCategory

mwe = namedtuple("mwe", ["name", "description", "lemmas", "category",
                         "verb_indices"])

turkish_mwes = [
        mwe("ayvayı yemek", "kötü bir duruma düşmek", ["ayva", "ye"],
            MweCategory.VID, [False, True]),
        mwe("ortaya çıkmak", "yokken var olmak, meydana çıkmak, türemek",
            ["orta", "çık"], MweCategory.VID, [False, True]),
        mwe("yer almak", "bir işi hazırlayanlar arasında bulunmak.",
            ["yer", "al"], MweCategory.VID, [False, True]),
        mwe("dikkat çekmek", "ilgi toplamak, göze batmak, fark edilmek.",
            ["dikkat", "çek"], MweCategory.VID, [False, True])
]

english_mwes = [
        mwe("(to) give up", "cease making an effort; admit defeat",
            ["give", "up"], MweCategory.VPC, [True, False]),
        mwe("let (someone) know", "to give information to (someone)",
            ["let", "know"], MweCategory.VPC, [False, True])
]

turkey_time = datetime.datetime.now()
mwe_date = date(turkey_time.year, turkey_time.month, turkey_time.day)
for mwe in turkish_mwes:
    add_mwe(mwe.name, mwe.description, Language.TURKISH, mwe_date, mwe.lemmas,
            mwe.category, mwe.verb_indices)
    mwe_date += datetime.timedelta(days=1)

mwe_date = date(turkey_time.year, turkey_time.month, turkey_time.day)
for mwe in english_mwes:
    add_mwe(mwe.name, mwe.description, Language.ENGLISH, mwe_date, mwe.lemmas,
            mwe.category, mwe.verb_indices)
    mwe_date += datetime.timedelta(days=1)
