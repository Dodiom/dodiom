import itertools
import threading
from abc import ABC, abstractmethod
from functools import lru_cache
from typing import List, Tuple, Dict, Optional
from fnmatch import fnmatch

import tokenizations

from i18n import Language
from models import Mwe


class Parsed:
    def __init__(self, language: Language, text: str, tokens: List[str],
                 token_positions: List[Tuple[int, int]],
                 lemmas: List[str]):
        self.language = language
        self.text = text
        self.tokens = tokens
        self.token_positions = token_positions
        self.lemmas = lemmas

    def contains_mwe(self, mwe: Mwe) -> bool:
        return self.contains_mwe_with_lemmas(mwe.lemmas)

    def contains_mwe_with_lemmas(self, lemmas: List[str]) -> bool:
        all_lemmas_exist = True

        for lemma in lemmas:
            this_lemma_exists = False
            for possible_lemma in lemma.split("|"):
                if "*" in possible_lemma or "?" in possible_lemma:
                    if any([fnmatch(parsed_lemma, possible_lemma) for parsed_lemma in self.lemmas]):
                        this_lemma_exists = True
                    elif any([fnmatch(parsed_token, possible_lemma) for parsed_token in self.tokens]):
                        this_lemma_exists = True
                else:
                    if any([parsed_lemma == possible_lemma for parsed_lemma in self.lemmas]):
                        this_lemma_exists = True
            all_lemmas_exist = all_lemmas_exist and this_lemma_exists

        return all_lemmas_exist

    def get_mwe_indices(self, mwe: Mwe) -> Tuple:
        if not self.contains_mwe(mwe):
            raise AssertionError("Mwe should be in parsed sentence.")

        mwe_lemma_positions: Dict[str, List[int]] = dict()
        for ix_tm, mwe_lemma in enumerate(mwe.lemmas):
            mwe_lemma_positions[mwe_lemma] = []
            for possible_lemma in mwe_lemma.split("|"):
                if "*" in possible_lemma or "?" in possible_lemma:
                    for ix, lemma in enumerate(self.lemmas):
                        if fnmatch(lemma, possible_lemma):
                            mwe_lemma_positions[mwe_lemma].append(ix)
                    for ix, token in enumerate(self.tokens):
                        if fnmatch(token, possible_lemma):
                            mwe_lemma_positions[mwe_lemma].append(ix)
                else:
                    for ix, lemma in enumerate(self.lemmas):
                        if lemma == possible_lemma:
                            mwe_lemma_positions[mwe_lemma].append(ix)

        mwe_instances = list(itertools.product(*[x for x in mwe_lemma_positions.values()]))
        mwe_instances_sorted = sorted(mwe_instances, key=lambda x: max(x) - min(x))
        return mwe_instances_sorted[0]

    def get_mwe_tokens(self, mwe: Mwe) -> List[str]:
        mwe_indices = self.get_mwe_indices(mwe)
        return [self.tokens[x] for x in mwe_indices]


class Parser(ABC):
    def __init__(self):
        self.parser_lock = threading.Lock()
        self.language = None

    @abstractmethod
    def get_sentence_count(self, text: str):
        pass

    @abstractmethod
    def lemmatize(self, text: str, mwe: Optional[Mwe] = None) -> Tuple[List[str], List[str]]:
        pass

    @lru_cache(maxsize=None)
    def parse(self, text: str, mwe: Mwe = None) -> Parsed:
        with self.parser_lock:
            tokens, lemmas = self.lemmatize(text, mwe)
            # print("Language:", self.language)
            # print("Tokens:", tokens)
            # print("Lemmas:", lemmas)
            token_positions = tokenizations.get_original_spans(tokens, text)
            return Parsed(self.language, text, tokens, token_positions, lemmas)
