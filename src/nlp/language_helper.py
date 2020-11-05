from i18n import Language


def lowercase(word: str, language: Language) -> str:
    if language == Language.ENGLISH or language == Language.ITALIAN:
        return word.lower()
    elif language == Language.TURKISH:
        return turkish_lowercase(word)


def turkish_lowercase(word: str) -> str:
    lower_map = {
        ord(u'I'): u'ı',
        ord(u'İ'): u'i',
        ord(u'Ş'): u'ş',
        ord(u'Ç'): u'ç',
        ord(u'Ğ'): u'ğ',
        ord(u'Ü'): u'ü',
        ord(u'Ö'): u'ö'
    }
    return word.translate(lower_map).lower()
