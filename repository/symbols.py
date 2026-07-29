from dataclasses import dataclass, field


@dataclass(slots=True)
class Symbol:

    name: str

    kind: str

    file: str

    line: int

    parent: str | None = None

    docstring: str = ""


@dataclass(slots=True)
class Import:

    module: str

    name: str

    alias: str | None

    file: str

    line: int


@dataclass(slots=True)
class ParsedFile:

    file: str

    symbols: list[Symbol] = field(default_factory=list)

    imports: list[Import] = field(default_factory=list)