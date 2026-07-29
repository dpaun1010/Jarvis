from sentence_transformers import SentenceTransformer
import chromadb


class VectorMemory:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.client = chromadb.PersistentClient(
            path="memory/database"
        )

        self.collection = self.client.get_or_create_collection(
            "deepjarvis"
        )

    def add(self, text: str):

        embedding = self.model.encode(text).tolist()

        self.collection.add(
            ids=[str(self.collection.count())],
            documents=[text],
            embeddings=[embedding]
        )

    def search(self, query: str, limit=5):

        embedding = self.model.encode(query).tolist()

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=limit
        )

        return results


vector_memory = VectorMemory()