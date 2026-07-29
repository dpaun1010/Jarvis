from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class Document:

    title: str

    content: str

    source: str

    id: str = field(default_factory=lambda: str(uuid4()))

    created_at: datetime = field(default_factory=datetime.now)