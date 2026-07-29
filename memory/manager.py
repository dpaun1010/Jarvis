from memory.store import store
from memory.vector import vector_memory


class MemoryManager:

    def remember(self, text):

        store.add(text)

        vector_memory.add(text)

    def recall(self, query):

        return vector_memory.search(query)


memory = MemoryManager()