from exception import TTSException
from logger import logger
import sys

def get_accent_tld(user_input):
    try:
        accent_input = {
            'Australian': 'com.au',
            'South Africa': 'co.za',
            'British': 'co.uk',
            'Indian': 'co.in',
            'Canadian': 'ca',
            'Irish': 'ie',
            'Spanish': 'es'
        }
        tld=accent_input.get(user_input)
        return tld
    except Exception as e:
        raise TTSException(e,sys)
def get_accent_message():
    try:
        accent=['Australian','South Africa','British',
                'Indian','Canadian','Irish','Spanish']
        return accent
    except Exception as e:
        raise TTSException(e,sys) 
    