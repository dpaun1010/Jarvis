from collections import defaultdict
from dataclasses import dataclass, field


@dataclass(slots=True)
class GraphNode:
    name: str
    kind: str
    file: str
    line: int


@dataclass(slots=True)
class GraphEdge:
    source: str
    target: str
    relation: str


class RepositoryGraph:

    def __init__(self):

        self.nodes = {}

        self.edges = []

        self.outgoing = defaultdict(list)

        self.incoming = defaultdict(list)

    def clear(self):

        self.nodes.clear()
        self.edges.clear()
        self.outgoing.clear()
        self.incoming.clear()

    def add_node(self, node: GraphNode):

        self.nodes[node.name] = node

    def add_edge(self, edge: GraphEdge):

        self.edges.append(edge)

        self.outgoing[edge.source].append(edge)

        self.incoming[edge.target].append(edge)

    def neighbours(self, symbol):

        return self.outgoing.get(symbol, [])

    def referenced_by(self, symbol):

        return self.incoming.get(symbol, [])


graph = RepositoryGraph()