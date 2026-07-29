import chromadb

from sentence_transformers import SentenceTransformer


class KnowledgeStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="knowledge/database"
        )

        self.collection = self.client.get_or_create_collection(
            "knowledge"
        )

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def add(self, document_id, text):

        embedding = self.model.encode(text).tolist()

        self.collection.add(
            ids=[document_id],
            documents=[text],
            embeddings=[embedding]
        )

    def search(self, query, limit=5):

        embedding = self.model.encode(query).tolist()

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=limit
        )


store = KnowledgeStore()