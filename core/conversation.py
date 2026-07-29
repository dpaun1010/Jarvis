from collections import deque


class ConversationManager:

    def __init__(self, max_history=20):
        self.history = deque(maxlen=max_history)

    def add_user(self, message):
        self.history.append({
            "role": "user",
            "content": message
        })

    def add_assistant(self, message):
        self.history.append({
            "role": "assistant",
            "content": message
        })

    def clear(self):
        self.history.clear()

    def messages(self):
        return list(self.history)


conversation = ConversationManager()