from abc import ABC


class BaseDiarization(ABC):
    def load_model(self, kwargs):
        ...    