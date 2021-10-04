import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']
watsonVersion = os.environ['version']

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version=watsonVersion,
    authenticator=authenticator
)

language_translator.set_service_url(URL)

def english_to_french(english_text):
    """
    translate english to french
    """
    french_text_json = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = french_text_json["translations"][0]["translation"]
    return french_text

def french_to_english(french_text):
    """
    translate french to english
    """
    english_text_json = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = english_text_json["translations"][0]["translation"]
    return english_text

print(french_to_english("Bonjour"))
print(english_to_french("Hello"))
