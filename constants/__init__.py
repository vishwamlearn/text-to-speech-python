APPLICATION_NAME='text_to_speech'
ARTIFACT_DIR_KEY='artifact'
AUDIO_DIR='tts_audio'
TEXT_DIR='tts_text'

TEXT_FILE_NAME='userinput.txt'
from datetime import datetime

fmt="%Y-%m-%d-%H%M%S"
CURRENT_TIME_STAMP=f"{datetime.now().strftime(fmt)}"