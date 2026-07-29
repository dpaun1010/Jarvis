from pypdf import PdfReader

from knowledge.loaders.base import DocumentLoader


class PDFLoader(DocumentLoader):

    def load(self, path: str) -> str:

        reader = PdfReader(path)

        text = []

        for page in reader.pages:

            extracted = page.extract_text()

            if extracted:

                text.append(extracted)

        return "\n".join(text)