import ast
from pathlib import Path

from repository import ast_index
from repository.graph import (
    graph,
    GraphNode,
    GraphEdge,
)


class CallVisitor(ast.NodeVisitor):

    def __init__(self, current):

        self.current = current

    def visit_Call(self, node):

        target = None

        if isinstance(node.func, ast.Name):

            target = node.func.id

        elif isinstance(node.func, ast.Attribute):

            target = node.func.attr

        if target:

            graph.add_edge(

                GraphEdge(

                    self.current,

                    target,

                    "calls"

                )

            )

        self.generic_visit(node)


class RepositoryCallGraph:

    def build(self, root="."):

        graph.clear()

        repo = ast_index.build(root)

        for parsed in repo.files.values():

            for symbol in parsed.symbols:

                graph.add_node(

                    GraphNode(

                        symbol.name,

                        symbol.kind,

                        symbol.file,

                        symbol.line

                    )

                )

            try:

                source = Path(parsed.file).read_text(
                    encoding="utf-8",
                    errors="ignore"
                )

                tree = ast.parse(source)

            except Exception:

                continue

            for node in ast.walk(tree):

                if isinstance(
                    node,
                    (
                        ast.FunctionDef,
                        ast.AsyncFunctionDef,
                    ),
                ):

                    CallVisitor(node.name).visit(node)

        return graph


call_graph = RepositoryCallGraph()