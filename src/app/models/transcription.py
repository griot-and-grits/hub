from dataclasses import dataclass, Field


@dataclass
class WhisperSegment:
    id: int
    seek: int
    start: float
    end: float
    text: str
    tokens: list[int] = Field(default=list)
    temperature: float


@dataclass
class TranscriptionResponse:
    text: str
    language: str
    segments: list[WhisperSegment]
