from exception import TTSException
from logger import logger
from entity.config_entity import TTSConfig
from constants import TEXT_FILE_NAME,CURRENT_TIME_STAMP
from gtts import gTTS
import sys
import os
import base64

class TTSapplication():
    def __init__(self,app_config=TTSConfig()):
        try:
            self.config=app_config
            self.artifact_dir=app_config.artifact_dir
            self.audio_dir=app_config.audio_dir
            self.text_dir=app_config.text_dir
        except Exception as e:
            raise TTSException(e,sys)
    def text2speech(self,text,accent):
        try:
            text_filename=TEXT_FILE_NAME
            text_file_path=os.path.join(self.text_dir,TEXT_FILE_NAME)
            os.makedirs(self.text_dir,exist_ok=True)
            with open(text_file_path,"+a") as file:
                file.write(f'\n{text}')
            #create  object for gtts
            tts=gTTS(text=text,lang='en',tld=accent,slow=False)
            filename=f'converted_file{CURRENT_TIME_STAMP}.mp3'

            audio_path=os.path.join(self.audio_dir,filename)
            os.makedirs(self.audio_dir,exist_ok=True)
            tts.save(audio_path)
            
            with open(audio_path,'rb') as file:
                my_string=base64.b64encode(file.read())
            return my_string
        except Exception as e:
            raise TTSException(e,sys)

