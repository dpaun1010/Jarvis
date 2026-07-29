from docx import Document

from knowledge.loaders.base import DocumentLoader


class DOCXLoader(DocumentLoader):

    def load(self, path: str) -> str:

        document = Document(path)

        return "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )