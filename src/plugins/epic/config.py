from pydantic import BaseModel, Extra
from typing import List


class Config(BaseModel, extra=Extra.ignore):
    epic_subscribe_group: List[int]
    epic_subscribe_user: List[int]
