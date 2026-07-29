from pathlib import Path

from repository import ast_index


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
                file.file
                for file in self.repo.files.values()
                if text in Path(file.file).name.lower()
            ]
        )

    def classes(self, text: str):
        text = text.lower()

        results = []

        for parsed in self.repo.files.values():

            for symbol in parsed.symbols:

                if symbol.kind != "class":
                    continue

                if text in symbol.name.lower():

                    results.append(symbol)

        return results

    def functions(self, text: str):
        text = text.lower()

        results = []

        for parsed in self.repo.files.values():

            for symbol in parsed.symbols:

                if symbol.kind not in (
                    "function",
                    "async",
                ):
                    continue

                if text in symbol.name.lower():

                    results.append(symbol)

        return results

    def text(self, query: str):

        query = query.lower()

        results = []

        for parsed in self.repo.files.values():

            try:

                content = Path(parsed.file).read_text(
                    encoding="utf-8",
                    errors="ignore"
                )

            except Exception:
                continue

            if query in content.lower():

                results.append(parsed.file)

        return results


search = RepositorySearch()