from pydantic import BaseModel
from typing import List

class BioRequest(BaseModel):
    about_me: str

class BioResponse(BaseModel):
    bios: List[str]