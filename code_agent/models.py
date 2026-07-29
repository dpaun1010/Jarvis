from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass
class CodeTask:

    instruction: str

    project: Path

    created_at: datetime = datetime.now()