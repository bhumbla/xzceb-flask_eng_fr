import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['api_version']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(englishtext):
    ''' This function translates English text to French '''
    frenchtext = language_translator.translate(
        text=englishtext,
        model_id='en-fr').get_result()
    return frenchtext.get('translations')[0].get('translation')

def french_to_english(frenchtext):
    ''' This function translates English text to French '''
    englishtext = language_translator.translate(
        text=frenchtext,
        model_id='fr-en').get_result()
    return englishtext.get('translations')[0].get('translation')
