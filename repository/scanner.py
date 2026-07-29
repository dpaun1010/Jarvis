from pathlib import Path

from repository.filter import filter_engine
from repository.models import FileInfo


class RepositoryScanner:

    def scan(

        self,

        root="."

    ):

        root = Path(root)

        files = []

        for path in root.rglob("*"):

            if not filter_engine.allowed(path):

                continue

            try:

                lines = sum(

                    1

                    for _

                    in path.open(

                        encoding="utf-8",

                        errors="ignore"

                    )

                )

            except Exception:

                lines = 0

            files.append(

                FileInfo(

                    path,

                    path.stat().st_size,

                    path.suffix,

                    lines

                )

            )

        return files


scanner = RepositoryScanner()