from pathlib import Path

from tools.base import Tool


class FileSystemTool(Tool):

    name = "filesystem"

    description = "Read and write files."

    def run(self, action: str, path: str, content: str = ""):

        file = Path(path)

        if action == "read":

            return file.read_text(encoding="utf-8")

        elif action == "write":

            file.parent.mkdir(parents=True, exist_ok=True)

            file.write_text(content, encoding="utf-8")

            return "Saved"

        elif action == "exists":

            return file.exists()

        else:

            raise ValueError("Unknown filesystem action.")