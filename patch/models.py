from dataclasses import dataclass, field
from enum import Enum


class EditType(str, Enum):
    INSERT = "insert"
    REPLACE = "replace"
    DELETE = "delete"
    APPEND = "append"


@dataclass(slots=True)
class FileEdit:
    file: str
    edit_type: EditType
    target: str
    replacement: str
    reason: str


@dataclass(slots=True)
class PatchPlan:
    objective: str
    edits: list[FileEdit] = field(default_factory=list)