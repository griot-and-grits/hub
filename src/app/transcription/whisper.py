from app.models.transcription import TranscriptionResponse
from app.config import Config
from app.errors import TranscriptionLoadError, TranscriptionRuntimeError
from .base import BaseTranscription
from io import FileIO
import whisper
import os


class WhisperTranscription(BaseTranscription):
    def __init__(self, config: Config):
        self.config = config

    def load_model(self, name: str):
        try:
            whisper.load_model(name)
        except Exception as ex:
            msg = f"Unable to load model {name}"
            raise TranscriptionLoadError(msg) from ex
        finally:
            # do any teardown
            pass

    def _transcribe(self, file: str | FileIO) -> TranscriptionResponse:
        if type(file) is str:
            if not os.path.exists(file):
                msg = "File to transcribe does not exist."
                raise TranscriptionRuntimeError(msg)
        elif type(file) is FileIO:
            file.seek(0)

        whisper.transcribe(file)
