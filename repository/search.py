from pathlib import Path

from repository import ast_index
from repository.database import database


class RepositorySearch:

    def __init__(self):
        self.repo = None

    def build(self, root="."):
        self.repo = ast_index.build(root)
        return self

    def files(self, text: str):

        text = text.lower()

        return sorted(
            [
                file.path
                for file in database.all()
                if text in Path(file.path).name.lower()
            ]
        )

    def classes(self, text: str):

        text = text.lower()

        results = []

        for file in database.all():

            for symbol in file.symbols:

                if symbol.kind != "class":
                    continue

                if text in symbol.name.lower():
                    results.append(symbol)

        return results

    def functions(self, text: str):

        text = text.lower()

        results = []

        for file in database.all():

            for symbol in file.symbols:

                if symbol.kind not in ("function", "async"):
                    continue

                if text in symbol.name.lower():
                    results.append(symbol)

        return results

    def text(self, query: str):

        query = query.lower()

        results = []

        for file in database.all():

            if query in file.source.lower():
                results.append(file.path)

        return results


search = RepositorySearch()