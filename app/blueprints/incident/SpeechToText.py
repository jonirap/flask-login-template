import os

import speech_recognition as sr
from enum import Enum

from consts import SPEECH_FOLDER


class Language(Enum):
    HEBREW = 'he'
    ENGLISH = 'en'


def convert_audio_file(audio_file_path, language=Language.HEBREW):
    print 'final ', audio_file_path
    assert isinstance(language, Language)
    assert isinstance(audio_file_path, basestring)
    assert os.path.isfile(audio_file_path)

    r = sr.Recognizer()
    r.energy_threshold += 280
    with sr.AudioFile(audio_file_path) as source:
        audio = r.listen(source)
        print audio

    try:
        return r.recognize_google(audio, language=language.value)
    except sr.UnknownValueError:
        return ''
