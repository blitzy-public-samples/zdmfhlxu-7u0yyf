from pydantic import BaseModel
from typing import Optional

class RepositoryModel(BaseModel):
    name: str
    owner: str
    url: str
    stars_gained: int
    total_stars: int

class WeeklyScanModel(BaseModel):
    repository_id: str
    scan_date: str
    stars_gained: int
    total_stars: int

class ReportModel(BaseModel):
    generation_date: str
    file_name: str
    file_url: str