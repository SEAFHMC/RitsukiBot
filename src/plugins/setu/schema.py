from typing import Optional
from pydantic import BaseModel, Extra


class SetuJson(BaseModel, extra=Extra.ignore):
    code: int
    message: str
    pid: Optional[int]
    p: Optional[int]
    img_url: Optional[str]
