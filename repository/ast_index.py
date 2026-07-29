import ast
import hashlib
from pathlib import Path

from repository import index
from repository.database import RepositoryFile, database
from repository.symbols import ParsedFile, Symbol, Import


class SymbolVisitor(ast.NodeVisitor):

    def __init__(self, path: str, parsed: ParsedFile):
        self.path = path
        self.parsed = parsed
        self.current_class = None

    def visit_ClassDef(self, node: ast.ClassDef):

        bases = []

        for base in node.bases:
            try:
                bases.append(ast.unparse(base))
            except Exception:
                pass

        decorators = []

        for dec in node.decorator_list:
            try:
                decorators.append(ast.unparse(dec))
            except Exception:
                pass

        self.parsed.symbols.append(
            Symbol(
                name=node.name,
                kind="class",
                file=self.path,
                line=node.lineno,
                bases=bases,
                decorators=decorators,
                docstring=ast.get_docstring(node) or "",
            )
        )

        previous = self.current_class
        self.current_class = node.name

        self.generic_visit(node)

        self.current_class = previous

    def visit_FunctionDef(self, node: ast.FunctionDef):

        decorators = []

        for dec in node.decorator_list:
            try:
                decorators.append(ast.unparse(dec))
            except Exception:
                pass

        kind = "method" if self.current_class else "function"

        self.parsed.symbols.append(
            Symbol(
                name=node.name,
                kind=kind,
                file=self.path,
                line=node.lineno,
                parent=self.current_class,
                decorators=decorators,
                docstring=ast.get_docstring(node) or "",
            )
        )

        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):

        decorators = []

        for dec in node.decorator_list:
            try:
                decorators.append(ast.unparse(dec))
            except Exception:
                pass

        kind = "async_method" if self.current_class else "async_function"

        self.parsed.symbols.append(
            Symbol(
                name=node.name,
                kind=kind,
                file=self.path,
                line=node.lineno,
                parent=self.current_class,
                decorators=decorators,
                docstring=ast.get_docstring(node) or "",
            )
        )

        self.generic_visit(node)

    def visit_Import(self, node: ast.Import):

        for alias in node.names:
            self.parsed.imports.append(
                Import(
                    module=alias.name,
                    name=alias.name,
                    alias=alias.asname,
                    file=self.path,
                    line=node.lineno,
                )
            )

    def visit_ImportFrom(self, node: ast.ImportFrom):

        module = node.module or ""

        for alias in node.names:
            self.parsed.imports.append(
                Import(
                    module=module,
                    name=alias.name,
                    alias=alias.asname,
                    file=self.path,
                    line=node.lineno,
                )
            )


class ASTIndexer:

    def __init__(self):
        self.files = {}

    def build(self, root="."):

        self.files.clear()
        database.clear()

        repo = index.build(root)

        for info in repo.by_extension.get(".py", []):
            self.parse(info.path)

        return self

    def parse(self, path: Path):

        try:
            source = path.read_text(
                encoding="utf-8",
                errors="ignore",
            )

            tree = ast.parse(source)

        except Exception:
            return

        parsed = ParsedFile(str(path))

        SymbolVisitor(str(path), parsed).visit(tree)

        digest = hashlib.sha256(source.encode()).hexdigest()

        database.add(
            RepositoryFile(
                path=str(path),
                source=source,
                symbols=parsed.symbols,
                imports=parsed.imports,
                hash=digest,
                modified=path.stat().st_mtime,
            )
        )

        self.files[str(path)] = parsed


ast_index = ASTIndexer()