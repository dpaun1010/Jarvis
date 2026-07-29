from pathlib import Path

from repository.config import (
    ALLOWED_EXTENSIONS,
    IGNORE_DIRS,
    MAX_FILE_SIZE,
    SOURCE_DIRS,
)


class RepositoryFilter:

    def allowed(self, path: Path) -> bool:

        if not path.is_file():
            return False

        # Ignore hidden directories and configured folders
        if any(part in IGNORE_DIRS for part in path.parts):
            return False

        # Only scan source directories (works even if project is nested)
        if SOURCE_DIRS:
            if not any(part in SOURCE_DIRS for part in path.parts[:-1]):
                return False

        # Allowed file extensions
        if path.suffix.lower() not in ALLOWED_EXTENSIONS:
            return False

        # Ignore very large files
        try:
            if path.stat().st_size > MAX_FILE_SIZE:
                return False
        except OSError:
            return False

        # Ignore binary files
        try:
            with path.open("rb") as f:
                chunk = f.read(1024)
                if b"\x00" in chunk:
                    return False
        except OSError:
            return False

        return True


filter_engine = RepositoryFilter()