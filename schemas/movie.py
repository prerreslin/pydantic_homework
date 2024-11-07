from pydantic import BaseModel, validator
from datetime import datetime

class MovieModel(BaseModel):
    title: str
    director: str
    release_year: int

    @validator("release_year")
    def validate_year(cls, value):
        current_year = datetime.now().year
        if value < current_year:
            raise ValueError(f"Release year {value} cannot be in the past")
        return value
