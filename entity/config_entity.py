from dataclasses import dataclass
import os

from constants import *

CURRENT_DIR=os.getchwd()


@dataclass
class TTSConfig:
    app_name:str=APPLICATION_NAME
    artifact_dir:str=os.path.join(CURRENT_DIR,app_name,ARTIFACT_DIR_KEY)
    audio_dir:str=os.path.join(artifact_dir,AUDIO_DIR)
    text_dir:str=os.path.join(artifact_dir,TEXT_DIR)

