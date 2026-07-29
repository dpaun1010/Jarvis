from pathlib import Path

from knowledge.loaders.pdf_loader import PDFLoader
from knowledge.loaders.docx_loader import DOCXLoader
from knowledge.loaders.text_loader import TextLoader


class LoaderFactory:

    def __init__(self):

        self.loaders = {
            ".pdf": PDFLoader(),
            ".docx": DOCXLoader(),
            ".txt": TextLoader(),
            ".md": TextLoader()
        }

    def load(self, path: str):

        extension = Path(path).suffix.lower()

        loader = self.loaders.get(extension)

        if loader is None:

            raise ValueError(
                f"No loader available for '{extension}'."
            )

        return loader.load(path)


factory = LoaderFactory()