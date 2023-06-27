from pydantic import BaseModel
from typing import List,Dict

class Course(BaseModel):
    name: str
    date: int
    description: str
    domain: List[str]
    chapters: List[dict]
    ratings: Dict[str, int] = {}

class Chapter(BaseModel):
    name: str
    text: str

class Ratings(BaseModel):
    ratings: dict

class Overview(BaseModel):
    overview: str