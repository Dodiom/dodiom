from datetime import datetime

from i18n import Language
from models import Mwe, MweCategory
from nlp.parsing import parser

mwe = Mwe(name="pull (one's) leg",
          meaning="example meaning",
          language=Language.ENGLISH,
          date=datetime.now().date(),
          lemmas=["pull", "my|your|his|her|its|*s", "leg"],
          category=MweCategory.VID)

sentence = "Please stop pulling my leg."
parsed = parser.parse(mwe.language, sentence)

parsed.get_mwe_indices(mwe)

lemmas = input("Lemmas > ").split(" ")

while True:
    sentence = input("Sentence > ")

    mwe = Mwe(name="example mwe",
              meaning="example meaning",
              language=Language.ENGLISH,
              date=datetime.now().date(),
              lemmas=lemmas,
              category=MweCategory.VID)
    parsed = parser.parse(mwe.language, sentence)
    print(parsed.lemmas)
    print(parsed.contains_mwe(mwe))
    print(parsed.get_mwe_indices(mwe))
    print(parsed.get_mwe_tokens(mwe))
