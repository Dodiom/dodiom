from i18n import Language

from nlp.english.parser import EnglishParser
from nlp.turkish.parser import TurkishParser
from nlp.italian.parser import ItalianParser
from config import mwexpress_config

if mwexpress_config.language == Language.ENGLISH:
    parser = EnglishParser()
elif mwexpress_config.language == Language.TURKISH:
    parser = TurkishParser()
elif mwexpress_config.language == Language.ITALIAN:
    parser = ItalianParser()
