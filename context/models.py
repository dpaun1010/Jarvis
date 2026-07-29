from dataclasses import dataclass, field


@dataclass(slots=True)
class ContextChunk:
    file: str
    reason: str
    source: str


@dataclass(slots=True)
class ContextPackage:
    objective: str
    chunks: list[ContextChunk] = field(default_factory=list)