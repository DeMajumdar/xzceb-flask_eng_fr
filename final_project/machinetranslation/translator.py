# ```py
# import json
# from ibm_watson import LanguageTranslatorV3
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# import os
# from dotenv import load_dotenv

# load_dotenv()

# apikey = os.environ['apikey']
# url = os.environ['url']
# ```
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('54HG78KNumwl61FBF2sgX43KplwxNMOWKXmbw0Dv2QIw')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com/instances/41a2ca48-09d2-4baa-8aa6-ae66f4cd1bc6')

def english_to_french(english_text):
    """
    Translates English text to French.
    :param english_text: The English text to translate.
    :return: The translated French text.
    """
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()

    french_text = translation['translations'][0]['translation']

    return french_text

def french_to_english(french_text):
    """
    Translates French text to English.
    :param french_text: The French text to translate.
    :return: The translated English text.
    """
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()

    english_text = translation['translations'][0]['translation']

    return english_text