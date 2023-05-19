import unittest
from translator import english_to_french, french_to_english

class TranslatorTests(unittest.TestCase):
    def test_english_to_french(self):
        # Test translation of 'Hello'
        english_text = 'Hello'
        expected_translation = 'Bonjour'
        result = english_to_french(english_text)
        self.assertEqual(result, expected_translation)

        # Test translation of 'OpenAI'---------------------------
        english_text = 'OpenAI'
        expected_translation = 'OpenAI'  # Assuming no translation available for 'OpenAI'
        result = english_to_french(english_text)
        self.assertEqual(result, expected_translation)

    def test_french_to_english(self):
        # Test translation of 'Bonjour'
        french_text = 'Bonjour'
        expected_translation = 'Hello'
        result = french_to_english(french_text)
        self.assertEqual(result, expected_translation)

        # Test translation of 'OpenAI'
        french_text = 'OpenAI'
        expected_translation = 'OpenAI'  # Assuming no translation available for 'OpenAI'
        result = french_to_english(french_text)
        self.assertEqual(result, expected_translation)

if __name__ == '__main__':
    unittest.main()

