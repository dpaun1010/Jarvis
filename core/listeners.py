from core.events import bus
from core.logger import logger
from core.event_types import *


def on_user_message(message):

    logger.info(f"User -> {message}")


def on_assistant_message(message):

    logger.info(f"Assistant -> {message}")


def on_tool_started(tool):

    logger.info(f"Executing {tool}")


def on_tool_finished(tool):

    logger.info(f"{tool} completed")


bus.subscribe(USER_MESSAGE, on_user_message)

bus.subscribe(ASSISTANT_MESSAGE, on_assistant_message)

bus.subscribe(TOOL_STARTED, on_tool_started)

bus.subscribe(TOOL_FINISHED, on_tool_finished)