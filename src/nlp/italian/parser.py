from functools import lru_cache
from typing import Optional, Tuple, List

import nltk
import tokenizations

from i18n import Language
from models import Mwe
from nlp.parser import Parser, Parsed
from nlp.italian.lemma import it_lemmatizer


class ItalianParser(Parser):
    def __init__(self):
        super(ItalianParser, self).__init__()
        self.language = Language.ITALIAN

    def get_sentence_count(self, text: str):
        return len(nltk.sent_tokenize(text, "italian"))

    def lemmatize(self, text: str, mwe: Optional[Mwe] = None) -> Tuple[List[str], List[str]]:
        return it_lemmatizer.lemmatize(text)
