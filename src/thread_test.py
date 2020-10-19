from datetime import datetime

from i18n import Language
from models import Mwe, MweCategory
from nlp.parsing import parser

import nltk
import zeyrek

analyzer = zeyrek.MorphAnalyzer()

while True:
    sentence = input("Enter sentence > ")
    parsed = parser.parse(Language.TURKISH, sentence)
    print(parsed.tokens)
    print(parsed.token_positions)
    print(parsed.lemmas)

mwe = Mwe(name="ayvayı yemek",
          meaning="kötü bir duruma düşmek",
          language=Language.TURKISH,
          date=datetime.now().date(),
          lemmas=["ayva", "yemek"],
          category=MweCategory.VID)

parsed = parser.parse(Language.TURKISH, "İşte şimdi elmayı yedim ve yediğim bu şey bir ayvadır.")
print(parsed.lemmas)
print(parsed.tokens)
print(parsed.get_mwe_indices(mwe))

