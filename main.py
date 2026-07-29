import tools
import core.listeners

from core.events import bus
from core.event_types import *


print()

bus.publish(
    SYSTEM_READY
)

while True:

    prompt = input("You : ")

    if prompt.lower() in ["exit", "quit"]:
        break

    bus.publish(
        USER_MESSAGE,
        prompt
    )

    bus.publish(
        TOOL_STARTED,
        "chat"
    )

    response = f"DeepJarvis > {prompt}"

    bus.publish(
        TOOL_FINISHED,
        "chat"
    )

    bus.publish(
        ASSISTANT_MESSAGE,
        response
    )

    print(response)