from pathlib import Path


class Patcher:

    def save(

        self,

        file,

        content

    ):

        Path(file).write_text(

            content,

            encoding="utf-8"

        )


patcher = Patcher()