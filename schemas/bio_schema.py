from pydantic import BaseModel
from typing import List

class BioRequest(BaseModel):
    text: str

class BioData(BaseModel):
    id: int
    content: str

class BioResponse(BaseModel):
    status: str
    message: str
    data: List[BioData]# Updated script
