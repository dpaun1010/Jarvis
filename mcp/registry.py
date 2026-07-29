class MCPRegistry:

    def __init__(self):

        self.clients = {}

    def register(
        self,
        name,
        client
    ):

        self.clients[name] = client

    def get(
        self,
        name
    ):

        return self.clients.get(name)

    def all(self):

        return self.clients


registry = MCPRegistry()