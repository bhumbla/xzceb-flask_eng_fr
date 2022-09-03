import unittest
from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase): 
    def testf2e(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') 
    def testnotf2e(self):
        self.assertNotEqual(french_to_english('Rien'), 'Something')

class TestEnglishToFrench(unittest.TestCase): 
    def teste2f(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def testnote2f(self):
        self.assertNotEqual(english_to_french('Something'), 'Rien')

unittest.main()