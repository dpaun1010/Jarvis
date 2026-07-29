from dataclasses import dataclass


@dataclass(slots=True)
class ExecutionResult:

    success: bool

    command: list[str]

    stdout: str

    stderr: str

    returncode: int