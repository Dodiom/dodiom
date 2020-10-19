import itertools
import logging
import threading
from functools import lru_cache
from typing import List, Tuple, Dict

import nltk
from nltk.stem.snowball import SnowballStemmer
import tokenizations
import zeyrek

from i18n import Language
from log import mwelog
from models import Mwe


def _flatten_str_list(list_to_flatten: List) -> List[str]:
    return [item for sublist in list_to_flatten for item in sublist]


class Parsed:
    def __init__(self, language: Language, text: str, tokens: List[str],
                 token_positions: List[Tuple[int, int]],
                 lemmas: List[List[str]]):
        self.language = language
        self.text = text
        self.tokens = tokens
        self.token_positions = token_positions
        self.lemmas = lemmas
        self.lemmas_flattened = set(_flatten_str_list(self.lemmas))
        print(self.lemmas)
        # mwelog.info(self.tokens)
        # mwelog.info(self.token_positions)
        mwelog.info(self.lemmas)
        mwelog.info(self.lemmas_flattened)
        # mwelog.info(self.lemmas_flattened)

    def contains_mwe(self, mwe: Mwe) -> bool:
        return all([lemma in self.lemmas_flattened for lemma in mwe.lemmas])

    def contains_mwe_with_lemmas(self, lemmas: List[str]) -> bool:
        return all([lemma in self.lemmas_flattened for lemma in lemmas])

    def get_mwe_indices(self, mwe: Mwe) -> Tuple:
        if not self.contains_mwe(mwe):
            raise AssertionError("Mwe should be in parsed sentence.")

        mwe_lemma_positions: Dict[str, List[int]] = dict()
        submission_lemmas = self.get_lemmas(mwe)
        for ix_tm, mwe_lemma in enumerate(mwe.lemmas):
            mwe_lemma_positions[mwe_lemma] = []
            for ix, lemma in enumerate(submission_lemmas):
                if lemma == mwe_lemma:
                    mwe_lemma_positions[mwe_lemma].append(ix)

        mwe_instances = list(itertools.product(*[x for x in mwe_lemma_positions.values()]))
        mwe_instances_sorted = sorted(mwe_instances, key=lambda x: max(x) - min(x))
        return mwe_instances_sorted[0]

    def get_mwe_tokens(self, mwe: Mwe) -> List[str]:
        mwe_indices = self.get_mwe_indices(mwe)
        return [self.tokens[x] for x in mwe_indices]

    def get_lemmas(self, mwe: Mwe = None) -> List[str]:
        if Mwe is None:
            return [lemma[0] for lemma in self.lemmas]
        else:
            if not self.contains_mwe(mwe):
                raise AssertionError("Mwe should be in parsed sentence.")
            lemma_list = []
            for lemma in self.lemmas:
                if len(lemma) == 1:
                    lemma_list.append(lemma[0])
                else:
                    appended_mwe_lemma = False
                    for mwe_lemma in mwe.lemmas:
                        if mwe_lemma in lemma:
                            appended_mwe_lemma = True
                            lemma_list.append(mwe_lemma)
                            break
                    if not appended_mwe_lemma:
                        lemma_list.append(lemma[0])
            return lemma_list


class Parser:
    def __init__(self):
        self.turkish_stemmer = zeyrek.MorphAnalyzer()
        self.english_stemmer = SnowballStemmer("english")
        self.parser_lock = threading.Lock()

    @staticmethod
    def get_sentence_count(language: Language, text: str):
        if language == Language.ENGLISH:
            return len(nltk.sent_tokenize(text))
        elif language == Language.TURKISH:
            return len(nltk.sent_tokenize(text, "turkish"))

    @lru_cache(maxsize=None)
    def parse(self, language: Language, text: str,
              mwe_lemmas: str = None) -> Parsed:
        with self.parser_lock:
            mwelog.info("Parsing cache miss")
            if language == Language.ENGLISH:
                tokens = nltk.word_tokenize(text)
                token_positions = tokenizations.get_original_spans(tokens, text)
                lemmas = [[self.english_stemmer.stem(token)] for token in tokens]
                return Parsed(language, text, tokens, token_positions, lemmas)
            elif language == Language.TURKISH:
                tokens = nltk.word_tokenize(text, "turkish")
                token_positions = tokenizations.get_original_spans(tokens, text)
                lemmas = [self._get_tr_stem(token) for token in tokens]
                parsed = Parsed(language, text, tokens, token_positions, lemmas)

                if mwe_lemmas is not None:
                    if not parsed.contains_mwe_with_lemmas(mwe_lemmas.split("|")):
                        logging.info("Refreshing stemmer")
                        self.turkish_stemmer = zeyrek.MorphAnalyzer()
                        self.turkish_stemmer = zeyrek.MorphAnalyzer()
                        token_positions = tokenizations.get_original_spans(tokens, text)
                        lemmas = [self._get_tr_stem(token) for token in tokens]
                        parsed = Parsed(language, text, tokens, token_positions, lemmas)

                return parsed

    @lru_cache(maxsize=None)
    def _get_tr_stem(self, word: str) -> List[str]:
        stem = self.turkish_stemmer.lemmatize(word)
        if len(stem) > 0:
            return stem[0][1]
        else:
            return [""]


parser = Parser()
