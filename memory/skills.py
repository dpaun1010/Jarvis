from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict
from uuid import uuid4


@dataclass
class Skill:

    id: str = field(default_factory=lambda: str(uuid4()))
    name: str = ""
    description: str = ""
    category: str = ""
    created_at: datetime = field(default_factory=datetime.now)


class SkillManager:

    def __init__(self):

        self.skills: Dict[str, Skill] = {}

    def add(self, skill: Skill):

        self.skills[skill.name] = skill

    def remove(self, name: str):

        self.skills.pop(name, None)

    def get(self, name: str):

        return self.skills.get(name)

    def all(self):

        return list(self.skills.values())


manager = SkillManager()