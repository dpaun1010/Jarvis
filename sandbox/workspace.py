import shutil
from pathlib import Path
from tempfile import mkdtemp


class Workspace:

    def __init__(self):
        self.root = None
        self.original = None

    def create(self, project_path):

        self.original = Path(project_path).resolve()

        temp = Path(mkdtemp(prefix="deepjarvis_"))

        self.root = temp / self.original.name

        shutil.copytree(
            self.original,
            self.root,
            dirs_exist_ok=True,
        )

        return self.root

    def cleanup(self):

        if self.root:

            shutil.rmtree(
                self.root.parent,
                ignore_errors=True,
            )

            self.root = None

    def resolve(self, relative):

        return self.root / relative


workspace = Workspace()