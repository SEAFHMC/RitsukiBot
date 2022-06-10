from pydantic import BaseModel, Extra
from typing import List


class Config(BaseModel, extra=Extra.ignore):
    sixty_subscribe_group: List[int]
