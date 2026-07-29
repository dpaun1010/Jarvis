from pathlib import Path


class ProjectFiles:

    def all(self, root: str):

        root = Path(root)

        files = []

        for file in root.rglob("*"):

            if file.is_file():

                files.append(file)

        return files

    def read(self, file):

        return Path(file).read_text(
            encoding="utf-8",
            errors="ignore"
        )

    def write(self, file, content):

        Path(file).write_text(
            content,
            encoding="utf-8"
        )


project = ProjectFiles()