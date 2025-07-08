from .base import BaseDiarization
from app.config import Config
from pyannote.audio import Pipeline

class PyannoteDiarization(BaseDiarization):
    def __init__(self, config: Config, model: str):
        self.model = model
        self.config = config

    def _load_model(self):
        """ """
        if hasattr(self, "model"):
            self.pipeline = Pipeline.from_pretrained(checkpoint_path=self.model)
