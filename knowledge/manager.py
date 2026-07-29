from knowledge.document import Document
from knowledge.chunker import chunker
from knowledge.vector_store import store


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

    def search(self, query):

        return store.search(query)


manager = KnowledgeManager()