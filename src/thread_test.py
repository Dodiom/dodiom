from datetime import datetime

from i18n import Language
from models import Mwe, MweCategory
from nlp.parsing import parser

lemmas = input("Lemmas > ").split(" ")

while True:
    sentence = input("Sentence > ")

    mwe = Mwe(name="example mwe",
              meaning="example meaning",
              language=Language.TURKISH,
              date=datetime.now().date(),
              lemmas=lemmas,
              category=MweCategory.VID)
    parsed = parser.parse(mwe.language, sentence)
    print(parsed.lemmas)
    print(parsed.contains_mwe(mwe))
    print(parsed.get_mwe_indices(mwe))
    print(parsed.get_mwe_tokens(mwe))
