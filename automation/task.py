from dataclasses import dataclass, field
from datetime import datetime
from typing import Callable
from uuid import uuid4


@dataclass
class Task:

    name: str
    action: Callable[[], None]

    priority: int = 5
    retries: int = 0
    delay: int = 0
    status: str = "PENDING"

    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=datetime.now)