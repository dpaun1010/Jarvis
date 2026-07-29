from pathlib import Path

from patch.models import (
    FileEdit,
    EditType,
)


class PatchEngine:

    def apply(self, edit: FileEdit):

        path = Path(edit.file)

        if not path.exists():
            raise FileNotFoundError(edit.file)

        source = path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

        updated = source

        if edit.edit_type == EditType.APPEND:

            updated = source + edit.replacement

        elif edit.edit_type == EditType.REPLACE:

            if edit.target not in source:
                raise ValueError(
                    f"Target not found: {edit.target}"
                )

            updated = source.replace(
                edit.target,
                edit.replacement,
                1,
            )

        elif edit.edit_type == EditType.INSERT:

            if edit.target not in source:
                raise ValueError(
                    f"Target not found: {edit.target}"
                )

            updated = source.replace(
                edit.target,
                edit.target + edit.replacement,
                1,
            )

        elif edit.edit_type == EditType.DELETE:

            if edit.target not in source:
                raise ValueError(
                    f"Target not found: {edit.target}"
                )

            updated = source.replace(
                edit.target,
                "",
                1,
            )

        return source, updated


patch_engine = PatchEngine()