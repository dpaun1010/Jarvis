from pathlib import Path


class FileEditor:

    def read(self, path: str):

        return Path(path).read_text(
            encoding="utf-8"
        )

    def write(self, path: str, content: str):

        file = Path(path)

        file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        file.write_text(
            content,
            encoding="utf-8"
        )

    def append(self, path: str, content: str):

        with open(
            path,
            "a",
            encoding="utf-8"
        ) as file:

            file.write(content)


editor = FileEditor()