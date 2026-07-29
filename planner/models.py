from dataclasses import dataclass, field


@dataclass(slots=True)
class PlannedFile:
    path: str
    reason: str
    confidence: float


@dataclass(slots=True)
class PlannedStep:
    order: int
    description: str


@dataclass(slots=True)
class ExecutionPlan:
    objective: str
    files: list[PlannedFile] = field(default_factory=list)
    steps: list[PlannedStep] = field(default_factory=list)
    confidence: float = 0.0