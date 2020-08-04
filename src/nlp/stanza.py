import stanza
from stanza import Document

from i18n import Language

nlp_en = stanza.Pipeline('en')
nlp_tr = stanza.Pipeline('tr')


def process_sentence(language: Language, sentence: str) -> Document:
    if language == Language.ENGLISH:
        return nlp_en(sentence)
    elif language == Language.TURKISH:
        return nlp_tr(sentence)
    else:
        raise NotImplemented("Language not supported")
