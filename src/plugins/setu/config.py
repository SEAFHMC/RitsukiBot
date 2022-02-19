from pydantic import BaseModel, Extra


class Config(BaseModel, extra=Extra.ignore):
    setu_recall_time: int
