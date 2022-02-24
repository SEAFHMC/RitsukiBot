from pydantic import BaseModel, Extra


class Config(BaseModel, extra=Extra.ignore):
    rss_url: str
