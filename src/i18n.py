from enum import Enum, auto
import random

from i18n_tokens import Token
from nlp.english.translation import en_translations, en_congrats_messages
from nlp.turkish.translation import tr_translations, tr_congrats_messages
from nlp.italian.translation import it_translations, it_congrats_messages


class Language(Enum):
    ENGLISH = auto()
    TURKISH = auto()
    ITALIAN = auto()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get(self, token: Token):
        if self == Language.ENGLISH:
            return en_translations[token]
        elif self == Language.TURKISH:
            return tr_translations[token]
        elif self == Language.ITALIAN:
            return it_translations[token]


def get_random_congrats_message(language: Language) -> str:
    if language == Language.ENGLISH:
        return en_congrats_messages[random.randint(0, len(en_congrats_messages) - 1)]
    elif language == Language.TURKISH:
        return tr_congrats_messages[random.randint(0, len(tr_congrats_messages) - 1)]
    elif language == Language.ITALIAN:
        return it_congrats_messages[random.randint(0, len(it_congrats_messages) - 1)]
