from memory.vector import vector_memory


class ContextRetriever:

    def retrieve(
        self,
        query: str,
        limit: int = 5
    ):

        try:

            results = vector_memory.search(
                query,
                limit
            )

            documents = results.get(
                "documents",
                [[]]
            )[0]

            return "\n".join(documents)

        except Exception:

            return ""


context = ContextRetriever()