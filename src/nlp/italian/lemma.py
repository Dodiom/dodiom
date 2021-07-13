from typing import List

import requests

from config import mwexpress_config


class ItalianLemmatizer:
    def __init__(self):
        self.lang_server = f"{mwexpress_config.it_lang_server}/tint"

    def lemmatize(self, text: str) -> (List[str], List[List[str]]):
        resp = requests.get(self.lang_server, params={'text': text}).json()
        tokens = []
        lemmas = []
        for token in resp["sentences"][0]["tokens"]:
            tokens.append(token["originalText"])
            if token["lemma"] != "[PUNCT]":
                lemmas.append(token["lemma"])
            else:
                lemmas.append(token["originalText"])
        return tokens, lemmas


it_lemmatizer = ItalianLemmatizer()
