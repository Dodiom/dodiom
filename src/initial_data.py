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
            ["dikkat", "çek"], MweCategory.VID, [False, True]),
        mwe("öne sürmek", "ortaya bir düşünce atmak.",
            ["ön", "sür"], MweCategory.VID, [False, True]),
        mwe("ortaya koymak", "yapmak, yaratmak, açıklamak, kaybetmeyi göze almak.",
            ["orta", "koy"], MweCategory.VID, [False, True]),
        mwe("ele almak", "bir konuyu incelemek, araştırmak, bir şey üzerinde çalışmaya başlamış olmak.",
            ["el", "al"], MweCategory.VID, [False, True]),
        mwe("yol açmak", "bir olayın nedeni olmak, bir olayın başlamasına sebep olmak, öncülük etmek.",
            ["yol", "aç"], MweCategory.VID, [False, True]),
        mwe("ileri sürmek", "üzerinde görüşülmek, tartışılmak üzere bir düşünce belirtmek.",
            ["ileri", "sür"], MweCategory.VID, [False, True]),
        mwe("meydana gelmek", "oluşmak, vücut bulmak, bir eylemin gerçekleşmesi.",
            ["meydan", "gel"], MweCategory.VID, [False, True]),
        mwe("karşı çıkmak", "ileri sürülen fikrin, tutulan yolun yanlış olduğunu söylemek, düşünceye katılmamak, cephe almak.",
            ["karşı", "çık"], MweCategory.VID, [False, True]),
        mwe("adım atmak", "bir işe ilk kez girişmek.",
            ["adım", "at"], MweCategory.VID, [False, True]),
        mwe("harekete geçmek", "bir işi yapmaya başlamak, bitirmek amacı ile bir işe girişmek.",
            ["hareket", "geç"], MweCategory.VID, [False, True]),
        mwe("ortaya atmak", "bir düşünceyi herkesin bilgisine sunmak.",
            ["orta", "at"], MweCategory.VID, [False, True]),
        mwe("göz yummak", "kabahatlerini, kusurlarını hoş karşılamak, görmezlikten gelmek, bağışlamak.",
            ["göz", "yum"], MweCategory.VID, [False, True]),
        mwe("karşı koymak", "engel olmaya çalışmak, direnmek, güç kullanarak dayanmak, boyun eğmemek.",
            ["karşı", "koy"], MweCategory.VID, [False, True]),
        mwe("el koymak", "zorla almak, sorumluluğu üstlenmek, yetkili organ bir malı veya bir kuruluşu kendi yönetimine almak.",
            ["el", "koy"], MweCategory.VID, [False, True]),
        mwe("hesap vermek", "herhangi bir davranışının ya da sözünün sebebini açıklamak, bir işin sorumluluğunu üstlenmek.",
            ["hesap", "ver"], MweCategory.VID, [False, True]),
        mwe("altını çizmek", "bir şeyin (daha çok sözün) önemini belirtmek, üzerine dikkati çekmek, vurgulamak.",
            ["alt", "çiz"], MweCategory.VID, [False, True]),

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
