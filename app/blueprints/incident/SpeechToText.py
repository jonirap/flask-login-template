import os

import speech_recognition as sr
from enum import Enum


class Language(Enum):
    HEBREW = 'he'
    ENGLISH = 'en'


def convert_audio_file(audio_file_path, language=Language.HEBREW):
    assert isinstance(language, Language)
    assert isinstance(audio_file_path, basestring)
    assert os.path.isfile(audio_file_path)

    r = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio = r.listen(source)

    return r.recognize_google(audio, language=language.value)


def record_and_convert(language=Language.HEBREW):
    assert isinstance(language, Language)

    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    return r.recognize_google(audio, language=language.value)
