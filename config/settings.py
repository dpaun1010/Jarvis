from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from dataclasses import dataclass


@dataclass
class SimpleSettings:
    model: str = "qwen3:8b"
    ollama_host: str = "http://localhost:11434"


simple_settings = SimpleSettings()


ROOT = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    APP_NAME: str = "DeepJarvis"
    VERSION: str = "1.0.0"

    MODEL: str = "qwen3:8b"
    OLLAMA_HOST: str = "http://localhost:11434"

    LOG_LEVEL: str = "INFO"

    DATA_DIR: Path = ROOT / "data"
    LOG_DIR: Path = ROOT / "logs"
    MEMORY_DIR: Path = ROOT / "memory"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()

settings.DATA_DIR.mkdir(exist_ok=True)
settings.LOG_DIR.mkdir(exist_ok=True)
settings.MEMORY_DIR.mkdir(exist_ok=True)

