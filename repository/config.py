from pathlib import Path


PROJECT_ROOT = Path.cwd()


SOURCE_DIRS = {

    "agent",
    "agents",
    "automation",
    "browser",
    "code_agent",
    "knowledge",
    "llm",
    "mcp",
    "memory",
    "repository",
    "scheduler",
    "tools",
    "vision",

}


IGNORE_DIRS = {

    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    "tests",
    "docs",
    "examples",
    "dist",
    "build",
    ".idea",
    ".vscode",
    ".pytest_cache",
    ".mypy_cache",

}


ALLOWED_EXTENSIONS = {

    ".py",
    ".md",
    ".txt",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".ini",

}


MAX_FILE_SIZE = 5 * 1024 * 1024