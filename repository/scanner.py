from pathlib import Path

from repository.models import FileInfo


IGNORE = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    ".idea",
    ".vscode",
    "dist",
    "build",
    ".pytest_cache",
    ".mypy_cache",
}


class RepositoryScanner:

    def scan(self, root: str):

        root = Path(root)

        files = []

        for path in root.rglob("*"):

            if not path.is_file():
                continue

            if any(
                part in IGNORE
                for part in path.parts
            ):
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

                    path=path,

                    size=path.stat().st_size,

                    suffix=path.suffix,

                    lines=lines

                )

            )

        return sorted(
            files,
            key=lambda x: str(x.path)
        )


scanner = RepositoryScanner()