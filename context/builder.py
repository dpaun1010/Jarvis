from context.models import (
    ContextChunk,
    ContextPackage,
)

from repository import (
    database,
    search,
)


class ContextBuilder:

    MAX_FILES = 8

    def build(self, objective: str):

        search.build(".")

        package = ContextPackage(objective)

        selected = set()

        candidates = []

        candidates.extend(search.files(objective))
        candidates.extend(search.text(objective))

        for path in candidates:

            if path in selected:
                continue

            repo_file = database.get(path)

            if repo_file is None:
                continue

            package.chunks.append(

                ContextChunk(

                    file=path,

                    reason="Repository search",

                    source=repo_file.source,

                )

            )

            selected.add(path)

            if len(package.chunks) >= self.MAX_FILES:
                break

        return package


context_builder = ContextBuilder()