import ast
from pathlib import Path

from repository import index
from repository.symbols import (
    ParsedFile,
    Symbol,
    Import,
)


class ASTIndexer:

    def __init__(self):

        self.files = {}

    def build(self, root="."):

        self.files.clear()

        repo = index.build(root)

        for info in repo.by_extension.get(".py", []):

            self.parse(info.path)

        return self

    def parse(self, path: Path):

        try:

            source = path.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            tree = ast.parse(source)

        except Exception:

            return

        parsed = ParsedFile(str(path))

        for node in ast.walk(tree):

            if isinstance(node, ast.ClassDef):

                parsed.symbols.append(

                    Symbol(

                        node.name,

                        "class",

                        str(path),

                        node.lineno,

                        docstring=ast.get_docstring(node) or ""

                    )

                )

            elif isinstance(node, ast.FunctionDef):

                parsed.symbols.append(

                    Symbol(

                        node.name,

                        "function",

                        str(path),

                        node.lineno,

                        docstring=ast.get_docstring(node) or ""

                    )

                )

            elif isinstance(node, ast.AsyncFunctionDef):

                parsed.symbols.append(

                    Symbol(

                        node.name,

                        "async",

                        str(path),

                        node.lineno,

                        docstring=ast.get_docstring(node) or ""

                    )

                )

            elif isinstance(node, ast.Import):

                for alias in node.names:

                    parsed.imports.append(

                        Import(

                            alias.name,

                            alias.name,

                            alias.asname,

                            str(path),

                            node.lineno

                        )

                    )

            elif isinstance(node, ast.ImportFrom):

                module = node.module or ""

                for alias in node.names:

                    parsed.imports.append(

                        Import(

                            module,

                            alias.name,

                            alias.asname,

                            str(path),

                            node.lineno

                        )

                    )

        self.files[str(path)] = parsed


ast_index = ASTIndexer()