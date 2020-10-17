import functools
import threading

import stanza
from stanza import Document

from i18n import Language

nlp_en = None
nlp_tr_pip = stanza.Pipeline('tr')

_nlp_tr_lock = threading.Lock()


@functools.lru_cache(128)
def nlp_tr(sentence: str) -> Document:
    with _nlp_tr_lock:
        return nlp_tr_pip(sentence)


def process_sentence(language: Language, sentence: str) -> Document:
    # if language == Language.ENGLISH:
    #     return nlp_en(sentence)
    # elif language == Language.TURKISH:
    if language == Language.TURKISH:
        return nlp_tr(sentence)
    else:
        raise NotImplemented("Language not supported")
