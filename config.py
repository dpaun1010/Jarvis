from dataclasses import dataclass
import os


@dataclass
class Settings:
    model: str = os.getenv("OLLAMA_MODEL", "qwen3:8b")
    ollama_host: str = os.getenv("OLLAMA_HOST", "http://localhost:11434")

    memory_path: str = "memory/database"

    max_history: int = 20

    temperature: float = 0.2


settings = Settings()
