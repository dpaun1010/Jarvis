from duckduckgo_search import DDGS

from tools.base import Tool


class SearchTool(Tool):

    name = "search"

    description = "Searches the internet."

    def run(self, query: str, limit: int = 5):

        results = []

        with DDGS() as ddgs:

            for item in ddgs.text(query, max_results=limit):

                results.append({
                    "title": item["title"],
                    "url": item["href"],
                    "body": item["body"]
                })

        return results