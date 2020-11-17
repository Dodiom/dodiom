import datetime
from collections import namedtuple
from datetime import date

from api.mwe import add_mwe
from i18n import Language
from models import MweCategory

mwe = namedtuple("mwe", ["name", "description", "lemmas", "category"])

turkish_mwes = [
        mwe("ayvayı yemek", "kötü bir duruma düşmek", ["ayva", "yemek"],
            MweCategory.VID),
        mwe("ortaya çıkmak", "yokken var olmak, meydana çıkmak, türemek",
            ["orta", "çık"], MweCategory.VID),
        mwe("yer almak", "bir işi hazırlayanlar arasında bulunmak.",
            ["yer", "al"], MweCategory.VID),
        mwe("öne sürmek", "ortaya bir düşünce atmak.",
            ["ön", "sür"], MweCategory.VID),
        mwe("ortaya koymak", "yapmak, yaratmak, açıklamak, kaybetmeyi göze almak.",
            ["orta", "koy"], MweCategory.VID),
        mwe("ele almak", "bir konuyu incelemek, araştırmak, bir şey üzerinde çalışmaya başlamış olmak.",
            ["el", "al"], MweCategory.VID),
        mwe("yol açmak", "bir olayın nedeni olmak, bir olayın başlamasına sebep olmak, öncülük etmek.",
            ["yol", "aç"], MweCategory.VID),
        mwe("ileri sürmek", "üzerinde görüşülmek, tartışılmak üzere bir düşünce belirtmek.",
            ["ileri", "sür"], MweCategory.VID),
        mwe("meydana gelmek", "oluşmak, vücut bulmak, bir eylemin gerçekleşmesi.",
            ["meydan", "gel"], MweCategory.VID),
        mwe("karşı çıkmak", "ileri sürülen fikrin, tutulan yolun yanlış olduğunu söylemek, düşünceye katılmamak, cephe almak.",
            ["karşı", "çık"], MweCategory.VID),
        mwe("adım atmak", "bir işe ilk kez girişmek.",
            ["adım", "at"], MweCategory.VID),
        mwe("ortaya atmak", "bir düşünceyi herkesin bilgisine sunmak.",
            ["orta", "at"], MweCategory.VID),
        mwe("göz yummak", "kabahatlerini, kusurlarını hoş karşılamak, görmezlikten gelmek, bağışlamak.",
            ["göz", "yum"], MweCategory.VID),
        mwe("el koymak", "zorla almak, sorumluluğu üstlenmek, yetkili organ bir malı veya bir kuruluşu kendi yönetimine almak.",
            ["el", "koy"], MweCategory.VID),
        mwe("hesap vermek", "herhangi bir davranışının ya da sözünün sebebini açıklamak, bir işin sorumluluğunu üstlenmek.",
            ["hesap", "ver"], MweCategory.VID),
        mwe("altını çizmek", "bir şeyin (daha çok sözün) önemini belirtmek, üzerine dikkati çekmek, vurgulamak.",
            ["alt", "çiz"], MweCategory.VID),
        mwe("yer vermek", "önemli saymak, imkân tanımak, önemli bir görev vermek, ağırlık vermek.",
            ["yer", "ver"], MweCategory.VID),
        mwe("ortaya çıkarmak", "delilleriyle göstermek, ispat etmek.",
            ["orta", "çıkar"], MweCategory.VID),
        mwe("rol oynamak", "bir işte önemli katkısı olmak, etkisi bulunmak.",
            ["rol", "oyna"], MweCategory.VID),
        mwe("üzerinde durmak", "bir işe önem vermek, o işle yakından ilgilenmek, uğraşmak.",
            ["üzeri", "dur"], MweCategory.VID),
        mwe("ağırlık vermek", "önem vermek, dikkati üzerinde yoğunlaştırmak.",
            ["ağırlık", "ver"], MweCategory.VID),
        mwe("ortadan kaldırmak", "saklamak, yok etmek, öldürmek.",
            ["orta", "kaldır"], MweCategory.VID),
        mwe("kolları sıvamak", "bir işi bütün gücüyle yapmaya hazırlanmak.",
            ["kol", "sıva"], MweCategory.VID),
        mwe("yola çıkmak", "herhangi bir şeyi esas almak, oradan başlamak.",
            ["yol", "çık"], MweCategory.VID),
        mwe("boyun eğmek", "isteyerek ya da istemeyerek uymak, katlanmak.",
            ["boyun", "eğ"], MweCategory.VID),
        mwe("meydana çıkmak", "ortaya çıkmak, görünmek, belli olmak, yetişmek, olmak.",
            ["meydan", "çık"], MweCategory.VID),
        mwe("iz bırakmak", "etkisini kalıcı duruma getirmek.",
            ["iz", "bırak"], MweCategory.VID),

]

english_mwes = [
        mwe("(to) give up", "cease making an effort; admit defeat",
            ["give", "up"], MweCategory.VPC),
        mwe("let (someone) know", "to give information to (someone)",
            ["let", "know"], MweCategory.VPC)
]

italian_mwes = [
    mwe("abbaiare alla luna", "Imprecare invano, gridare inutilmente contro qualcuno che è lontano e non può, perciò, sentirci",
        ['abbaiare', 'alla', 'luna'], MweCategory.VID),
    mwe("Acchiappare farfalle", "Fare cose inutili.",
        ['acchiappare', 'farfalla'], MweCategory.VID),
    mwe("Ingoiare una pillola", "Assoggettarsi a qualcosa di sgradevole.",
        ['ingoiare', 'una', 'pillola'], MweCategory.VID),
    mwe("Rifarsi la bocca", "Trovare un compenso a qualcosa di spiacevole.",
        ['rifare', 'la', 'bocca'], MweCategory.VID),
    mwe("Rimanere in sella", "Conservare la propria autorità.",
        ['rimanere', 'in', 'sella'], MweCategory.VID),
    mwe("Far leva", "Agire su un determinato elemento per ottenere qualcosa che si desidera.",
        ['fare', 'leva'], MweCategory.VID),
    mwe("Essere a cavallo", "Essere sicuro di raggiungere uno scopo.",
        ['essere', 'a', 'cavallo'], MweCategory.VID),
    mwe("Essere in vena", "Sentirsi nel pieno delle forze, dell'estro, nella condizione migliore per fare qualcosa.",
        ['essere', 'in', 'vena'], MweCategory.VID),
    mwe("Essere su un binario morto", "Essere in una situazione difficile e senza sbocchi.",
        ['essere', 'su', 'un', 'binario', 'morto'], MweCategory.VID),
    mwe("Voltare la faccia", "Scappare, cambiare direzione.",
        ['voltare', 'faccia'], MweCategory.VID),
    mwe("Gettare la spugna", "Arrendersi, rinunciare alla lotta.",
        ['gettare', 'la', 'spugna'], MweCategory.VID),
    mwe("Coltivare il proprio orto", "Occuparsi solo dei propri problemi, disinteressandosi di quelli altrui",
        ['il', 'proprio', 'orto'], MweCategory.VID),
    mwe("Buttare giù", "Inghiottire",
        ['buttare', 'giù'], MweCategory.VID),
    mwe("Mettere dentro", "Arrestare",
        ['mettere', 'dentro'], MweCategory.VID),
]

turkey_time = datetime.datetime.now()
# mwe_date = date(turkey_time.year, turkey_time.month, turkey_time.day)
# for mwe in turkish_mwes:
#     add_mwe(mwe.name, mwe.description, Language.TURKISH, mwe_date, mwe.lemmas,
#             mwe.category)
#     mwe_date += datetime.timedelta(days=1)
#
# mwe_date = date(turkey_time.year, turkey_time.month, turkey_time.day)
# for mwe in english_mwes:
#     add_mwe(mwe.name, mwe.description, Language.ENGLISH, mwe_date, mwe.lemmas,
#             mwe.category)
#     mwe_date += datetime.timedelta(days=1)

mwe_date = date(turkey_time.year, turkey_time.month, turkey_time.day)
for mwe in italian_mwes:
    add_mwe(mwe.name, mwe.description, Language.ITALIAN, mwe_date, mwe.lemmas,
            mwe.category)
    mwe_date += datetime.timedelta(days=1)
