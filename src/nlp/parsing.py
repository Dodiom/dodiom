import itertools
import threading
from functools import lru_cache
from typing import List, Tuple, Dict
from fnmatch import fnmatch

import nltk
from nltk.stem.snowball import SnowballStemmer
import tokenizations
import zeyrek

from i18n import Language
from models import Mwe
from nlp.italian.lemma import it_lemmatizer


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

    def contains_mwe(self, mwe: Mwe) -> bool:
        return self.contains_mwe_with_lemmas(mwe.lemmas)

    def contains_mwe_with_lemmas(self, lemmas: List[str]) -> bool:
        all_lemmas_exist = True

        for lemma in lemmas:
            this_lemma_exists = False
            for possible_lemma in lemma.split("|"):
                if "*" in possible_lemma or "?" in possible_lemma:
                    if any([fnmatch(parsed_lemma, possible_lemma) for parsed_lemma in self.lemmas_flattened]):
                        this_lemma_exists = True
                    elif any([fnmatch(parsed_token, possible_lemma) for parsed_token in self.tokens]):
                        this_lemma_exists = True
                else:
                    this_lemma_exists = any([parsed_lemma == possible_lemma for parsed_lemma in self.lemmas_flattened])
            all_lemmas_exist = all_lemmas_exist and this_lemma_exists

        return all_lemmas_exist

    def get_mwe_indices(self, mwe: Mwe) -> Tuple:
        if not self.contains_mwe(mwe):
            raise AssertionError("Mwe should be in parsed sentence.")

        mwe_lemma_positions: Dict[str, List[int]] = dict()
        submission_lemmas = self.get_lemmas(mwe)
        for ix_tm, mwe_lemma in enumerate(mwe.lemmas):
            mwe_lemma_positions[mwe_lemma] = []
            for possible_lemma in mwe_lemma.split("|"):
                if "*" in possible_lemma or "?" in possible_lemma:
                    for ix, lemma in enumerate(submission_lemmas):
                        if fnmatch(lemma, possible_lemma):
                            mwe_lemma_positions[mwe_lemma].append(ix)
                    for ix, token in enumerate(self.tokens):
                        if fnmatch(token, possible_lemma):
                            mwe_lemma_positions[mwe_lemma].append(ix)
                else:
                    for ix, lemma in enumerate(submission_lemmas):
                        if lemma == possible_lemma:
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
        elif language == Language.ITALIAN:
            return len(nltk.sent_tokenize(text, "italian"))

    @lru_cache(maxsize=None)
    def parse(self, language: Language, text: str,
              mwe_lemmas: str = None) -> Parsed:
        with self.parser_lock:
            # mwelog.info("Parsing cache miss")
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
                        # mwelog.info("Refreshing stemmer")
                        self.turkish_stemmer = zeyrek.MorphAnalyzer()
                        token_positions = tokenizations.get_original_spans(tokens, text)
                        lemmas = [self._get_tr_stem(token) for token in tokens]
                        parsed = Parsed(language, text, tokens, token_positions, lemmas)

                return parsed
            elif language == Language.ITALIAN:
                tokens, lemmas = it_lemmatizer.lemmatize(text)
                token_positions = tokenizations.get_original_spans(tokens, text)
                return Parsed(language, text, tokens, token_positions, lemmas)

    def _get_tr_stem(self, word: str) -> List[str]:
        stem = self.turkish_stemmer.lemmatize(word)
        if len(stem) > 0:
            return stem[0][1]
        else:
            return [""]


parser = Parser()
