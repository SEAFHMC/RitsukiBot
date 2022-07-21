from typing import Optional, List
from pydantic import BaseModel, Extra


class Data(BaseModel, extra=Extra.ignore):
    pid: Optional[int]
    p: Optional[int]
    img_url: Optional[str]


class SetuJson(BaseModel, extra=Extra.ignore):
    code: int
    message: str
    data: Optional[List[Data]]
