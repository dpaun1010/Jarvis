from dataclasses import dataclass, field


@dataclass(slots=True)
class RepositoryFile:
    path: str
    source: str
    symbols: list = field(default_factory=list)
    imports: list = field(default_factory=list)
    hash: str = ""
    modified: float = 0.0


class RepositoryDatabase:

    def __init__(self):
        self.files: dict[str, RepositoryFile] = {}

    def clear(self):
        self.files.clear()

    def add(self, repo_file: RepositoryFile):
        self.files[repo_file.path] = repo_file

    def get(self, path: str):
        return self.files.get(path)

    def all(self):
        return self.files.values()

    def __len__(self):
        return len(self.files)


database = RepositoryDatabase()