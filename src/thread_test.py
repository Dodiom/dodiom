from datetime import datetime

from i18n import Language
from models import Mwe, MweCategory
from nlp.italian.lemma import it_lemmatizer
from nlp.parsing import parser

mwe = Mwe(name="abbaiare alla luna",
          meaning="Imprecare invano, gridare inutilmente contro qualcuno che è lontano e non può, perciò, sentirci",
          language=Language.ITALIAN,
          date=datetime.now().date(),
          lemmas=['abbaiare', 'alla', 'luna'],
          category=MweCategory.VID)


it_lemmatizer.lemmatize("Abbaiare alla luna o roteare gatti non può curare una milza malata.")

parsed = parser.parse(Language.ITALIAN,
      "Abbaiare alla luna o roteare gatti non può curare una milza malata.")


print(mwe.lemmas)
print(parsed.lemmas)
print(parsed.lemmas_flattened)

print(parsed.contains_mwe(mwe))
