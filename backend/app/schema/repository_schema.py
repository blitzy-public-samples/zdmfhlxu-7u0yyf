from pydantic import BaseModel
from typing import Optional

class RepositorySchema(BaseModel):
    name: str
    owner: str
    url: str
    stars_gained: int
    total_stars: int

    class Config:
        # Add any additional configuration if needed
        pass