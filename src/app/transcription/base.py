from abc import ABC, abstractmethod
from app.models.transcription import TranscriptionResponse


class BaseTranscription(ABC):
    @abstractmethod
    def setup():
        """Setup the transcription layer."""

    @abstractmethod
    def transcribe() -> TranscriptionResponse:
        """Do a transcription active."""
