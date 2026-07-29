from pathlib import Path

from knowledge.document import Document
from knowledge.chunker import chunker
from knowledge.vector_store import store
from knowledge.loaders.loader_factory import factory


class KnowledgeManager:

    def add_document(self, title, source, content):

        document = Document(
            title=title,
            source=source,
            content=content
        )

        chunks = chunker.split(content)

        for index, chunk in enumerate(chunks):

            store.add(
                f"{document.id}_{index}",
                chunk
            )

        return document

    def add_file(self, path: str):

        text = factory.load(path)

        return self.add_document(
            title=Path(path).name,
            source=path,
            content=text
        )

    def search(self, query):

        return store.search(query)


manager = KnowledgeManager()