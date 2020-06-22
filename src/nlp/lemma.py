from typing import List
import stanza
from stanza.models.common.doc import Word

from i18n import Language

# stanza.download("en")
# stanza.download("tr")

nlp_en = stanza.Pipeline('en', processors='tokenize,pos,lemma')
nlp_tr = stanza.Pipeline('tr', processors='tokenize,pos,lemma')


def get_lemmas(lang: Language, sentence: str) -> List[str]:
    x: Word
    if lang == Language.ENGLISH:
        return [x.lemma for x in nlp_en(sentence).iter_words() if x.pos != "PUNCT"]
    elif lang == Language.TURKISH:
        return [x.lemma for x in nlp_tr(sentence).iter_words() if x.pos != "PUNCT"]


def get_words(lang: Language, sentence: str) -> List[str]:
    x: Word
    if lang == Language.ENGLISH:
        return [x.text for x in nlp_en(sentence).iter_words() if x.pos != "PUNCT"]
    elif lang == Language.TURKISH:
        return [x.text for x in nlp_tr(sentence).iter_words() if x.pos != "PUNCT"]
