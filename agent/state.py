from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class AgentState:

    goal: str

    completed: bool = False

    iterations: int = 0

    max_iterations: int = 10

    history: list = field(default_factory=list)

    created_at: datetime = field(default_factory=datetime.now)

    def add(self, item):

        self.history.append(item)