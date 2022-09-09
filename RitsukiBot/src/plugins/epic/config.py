from typing import Dict, List
import ujson as json
from pathlib import Path
from pydantic import BaseModel

ROOT = Path() / "data" / "epic"
ROOT.mkdir(parents=True, exist_ok=True)
config_path = ROOT / "config.json"

default_config = {"user": [], "group": []}


class ConfigModel(BaseModel):
    user: List[int]
    group: List[int]


class Config:
    def __init__(self) -> None:
        if not Path.exists(config_path):
            with open(config_path, "w", encoding="UTF-8") as f:
                f.write(json.dumps(default_config, indent=2))
            self.config = default_config
        else:
            with open(config_path, "r", encoding="UTF-8") as f:
                self.config = json.loads(f.read())
        return

    @classmethod
    def write_config(cls, config: Dict[str, List[int]]):
        with open(config_path, "w", encoding="UTF-8") as f:
            f.write(json.dumps(config))
        return

    def parse_config(self):
        return ConfigModel(**self.config)

    def add_user(self, user_id: int):
        if user_id not in self.config["user"]:
            self.config["user"].append(user_id)
        self.write_config(self.config)
        return

    def remove_user(self, user_id: int):
        if user_id in self.config["user"]:
            self.config["user"].remove(user_id)
        self.write_config(self.config)
        return

    def add_group(self, group_id: int):
        if group_id not in self.config["group"]:
            self.config["group"].append(group_id)
        self.write_config(self.config)
        return

    def remove_group(self, group_id: int):
        if group_id in self.config["group"]:
            self.config["group"].remove(group_id)
        self.write_config(self.config)
        return
