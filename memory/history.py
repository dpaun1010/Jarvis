from collections import deque


class ConversationHistory:

    def __init__(self):

        self.messages = deque(
            maxlen=20
        )

    def add_user(self, text):

        self.messages.append(
            {
                "role": "user",
                "content": text
            }
        )

    def add_assistant(self, text):

        self.messages.append(
            {
                "role": "assistant",
                "content": text
            }
        )

    def all(self):

        return list(self.messages)

    def clear(self):

        self.messages.clear()


history = ConversationHistory()