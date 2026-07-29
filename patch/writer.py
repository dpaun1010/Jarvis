from pathlib import Path


class PatchWriter:

    def write(
        self,
        path,
        source,
    ):

        Path(path).write_text(
            source,
            encoding="utf-8",
        )


writer = PatchWriter()