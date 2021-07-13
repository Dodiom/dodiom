import unittest
import nltk
from nlp.english.parser import EnglishParser


class EnglishParserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        nltk.download('punkt')

    def test_get_sentence_count(self):
        parser = EnglishParser()

        sentences = "I like apples. I watch TV."
        sentence_count = parser.get_sentence_count(sentences)
        self.assertEqual(2, sentence_count)


if __name__ == '__main__':
    unittest.main()
