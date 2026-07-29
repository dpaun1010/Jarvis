from collections import defaultdict
from hashlib import sha256
from pathlib import Path

from repository.scanner import scanner


class RepositoryIndex:

    def __init__(self):
        self.clear()

    def clear(self):
        self.files = []
        self.by_name = defaultdict(list)
        self.by_extension = defaultdict(list)
        self.by_relative = {}
        self.hashes = {}

    def build(self, root="."):

        self.clear()

        root = Path(root).resolve()

        for info in scanner.scan(root):

            absolute = info.path.resolve()

            try:
                relative = absolute.relative_to(root).as_posix()
            except ValueError:
                relative = absolute.name

            self.files.append(info)

            self.by_name[absolute.name].append(info)

            self.by_extension[info.suffix.lower()].append(info)

            self.by_relative[relative] = info

            try:
                digest = sha256(absolute.read_bytes()).hexdigest()
            except Exception:
                digest = ""

            self.hashes[relative] = digest

        return self

    def exists(self, relative_path):
        return relative_path in self.by_relative

    def get(self, relative_path):
        return self.by_relative.get(relative_path)

    def find(self, filename):
        return self.by_name.get(filename, [])

    def extensions(self):
        return sorted(self.by_extension.keys())

    def duplicates(self):
        return {
            name: files
            for name, files in self.by_name.items()
            if len(files) > 1
        }


index = RepositoryIndex()