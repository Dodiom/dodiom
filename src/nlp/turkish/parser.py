from typing import List, Optional, Tuple

import nltk
import zeyrek

from i18n import Language
from models import Mwe
from nlp.parser import Parser


class TurkishParser(Parser):
    def __init__(self):
        super(TurkishParser, self).__init__()
        self.turkish_stemmer = zeyrek.MorphAnalyzer()
        self.language = Language.TURKISH

    def get_sentence_count(self, text: str):
        return len(nltk.sent_tokenize(text, "italian"))

    def lemmatize(self, text: str, mwe: Optional[Mwe] = None) -> Tuple[List[str], List[str]]:
        tokens = nltk.word_tokenize(text, "turkish")
        lemmas = [self._get_tr_stem(token) for token in tokens]
        return tokens, lemmas

    def _get_tr_stem(self, word: str) -> str:
        stem = self.turkish_stemmer.lemmatize(word)
        if len(stem) > 0:
            return stem[0][1][0]
        else:
            return ""
