from dataclasses import dataclass
from datetime import datetime
from typing import Dict
import uuid


@dataclass
class Memory:

    id: str
    content: str
    metadata: Dict
    created_at: str


class MemoryStore:

    def __init__(self):

        self.memories = []

    def add(self, content: str, metadata=None):

        if metadata is None:
            metadata = {}

        memory = Memory(
            id=str(uuid.uuid4()),
            content=content,
            metadata=metadata,
            created_at=datetime.utcnow().isoformat()
        )

        self.memories.append(memory)

        return memory

    def all(self):

        return self.memories

    def clear(self):

        self.memories.clear()


store = MemoryStore()
