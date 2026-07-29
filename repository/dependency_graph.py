from collections import defaultdict
from pathlib import Path

from repository import ast_index


class DependencyGraph:

    def __init__(self):

        self.dependencies = defaultdict(set)

        self.reverse_dependencies = defaultdict(set)

    def build(self, root="."):

        self.dependencies.clear()

        self.reverse_dependencies.clear()

        repo = ast_index.build(root)

        modules = {}

        for file in repo.files.values():

            module = (

                Path(file.file)

                .with_suffix("")

                .as_posix()

                .replace("/", ".")

            )

            modules[module] = file.file

        for file in repo.files.values():

            source = file.file

            for imp in file.imports:

                target = modules.get(imp.module)

                if target:

                    self.dependencies[source].add(target)

                    self.reverse_dependencies[target].add(source)

        return self

    def imports_of(self, file):

        return sorted(self.dependencies.get(file, []))

    def imported_by(self, file):

        return sorted(self.reverse_dependencies.get(file, []))


dependency_graph = DependencyGraph()