from typing import Optional, Tuple, List

import nltk
from nltk import SnowballStemmer

from i18n import Language
from models import Mwe
from nlp.parser import Parser


class EnglishParser(Parser):
    def __init__(self):
        super(EnglishParser, self).__init__()
        self.english_stemmer = SnowballStemmer("english")
        self.language = Language.ENGLISH

    def get_sentence_count(self, text: str):
        return len(nltk.sent_tokenize(text))

    def lemmatize(self, text: str, mwe: Optional[Mwe] = None) -> Tuple[List[str], List[str]]:
        tokens = nltk.word_tokenize(text)
        lemmas = [self.english_stemmer.stem(token) for token in tokens]
        return tokens, lemmas
