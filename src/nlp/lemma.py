from typing import List
import stanza
from stanza.models.common.doc import Word, Document, Sentence

from i18n import Language

# stanza.download("en")
# stanza.download("tr")

nlp_en = stanza.Pipeline('en', processors='tokenize,mwt,pos,lemma')
nlp_tr = stanza.Pipeline('tr', processors='tokenize,mwt,pos,lemma')


def get_lemmas(lang: Language, sentence: str) -> List[str]:
    x: Word
    if lang == Language.ENGLISH:
        return [x.lemma for x in nlp_en(sentence).iter_words()]
    elif lang == Language.TURKISH:
        return [x.lemma for x in nlp_tr(sentence).iter_words()]


def get_words(lang: Language, sentence: str) -> List[str]:
    x: Word
    if lang == Language.ENGLISH:
        return [x.text for x in nlp_en(sentence).iter_words()]
    elif lang == Language.TURKISH:
        return [x.text for x in nlp_tr(sentence).iter_words()]
