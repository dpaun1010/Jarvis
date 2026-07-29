import requests


class MCPClient:

    def __init__(self):

        self.url = None

    def connect(self, url: str):

        self.url = url.rstrip("/")

    def tools(self):

        response = requests.get(
            f"{self.url}/tools"
        )

        response.raise_for_status()

        return response.json()

    def execute(
        self,
        tool: str,
        arguments: dict
    ):

        response = requests.post(

            f"{self.url}/execute",

            json={
                "tool": tool,
                "arguments": arguments
            }

        )

        response.raise_for_status()

        return response.json()


client = MCPClient()