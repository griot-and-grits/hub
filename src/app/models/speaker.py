from pydantic import BaseModel, Field
from pyannote.core import Segment


class Speaker(BaseModel):
    name: str = Field(default=..., description="Speaker name.")
    segment: Segment = Field(
        default=None, description="The segment of audio or snippet."
    )
