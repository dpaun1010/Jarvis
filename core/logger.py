from pathlib import Path
from loguru import logger
from config.settings import settings

logger.remove()

logger.add(
    Path(settings.LOG_DIR) / "jarvis.log",
    rotation="10 MB",
    retention="30 days",
    level=settings.LOG_LEVEL,
    enqueue=True
)

logger.add(
    lambda msg: print(msg, end=""),
    colorize=True,
    level=settings.LOG_LEVEL
)