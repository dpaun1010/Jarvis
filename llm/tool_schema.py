from dataclasses import dataclass, field


@dataclass
class ToolParameter:

    name: str
    type: str
    description: str
    required: bool = True


@dataclass
class ToolSchema:

    name: str
    description: str
    parameters: list[ToolParameter] = field(default_factory=list)