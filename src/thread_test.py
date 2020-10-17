import logging
import random
import threading
from datetime import datetime

from nlp.stanza import nlp_tr


def thread_function(name):
    messages = [
        "Hadi artık şu ayvayı yiyip kalkalım.",
        "Teyzesi köyden 10 dönüm yer almış.",
        "Ayvaları yiyip tabaklarını makineye yerleştirdiler.",
        "Bugün kaç ayva yedim ben bile sayamadım.",
        "İște şimdi ayvayı yedim.",
        "Ayva yemeyi çok seviyorum.",
        "İyi mi olur yoksa ayvayı mı yeriz göreceğiz.",
        "Bu durum ayvayı yediğimizin kanıtıdır.",
        "Hergün bir ayvayı limon sıkarak yemek sağlığa çok faydalıdır.",
        "Üniversitenin 2. döneminde birden verilen ödev sayısını görünce ayvayı yedi.",
        "Tabakta kalan son ayvayı yedim.",
        "Bugün tam 1 kilo ayva yedim.",
        "Ayva yemek istemiyorum, elma ya da muz var mı?",
        "Meydanın orta yerinden bir anda çıkıverdi.",
        "Bu hiç iyi olmadı, işte şimdi ayvayı yedik.",
        "Ayva yemek ister misin?",
        "Baharla birlikte tüm çiçekler ortaya çıktı.",
        "Yalanları birbir ortaya çıkti.",
        "Ekmek ayvasını yemek gerçekten daha kolay.",
        "Ayvayı yediğimin resmidir bu.",
        "Ayva yemek kalp damar hastalıkları başta olmak üzere birçok hastalığa iyi gelmektedir.",
    ]
    for i in range(10):
        msg = random.choice(messages)
        doc = nlp_tr(msg)
        #print(f'{msg}: {len(doc.sentences[0].tokens)}')
        #print(nlp_tr.cache_info())

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()
    start = datetime.now()
    for index in range(8):
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        thread.join()

    print(datetime.now() - start)
