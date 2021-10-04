import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertIsNone(english_to_french(None))
        self.assertNotEqual(english_to_french('Bonjour'), 'Hello')

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Hello'), 'Bonjour')
        self.assertIsNone(french_to_english(None))

unittest.main()