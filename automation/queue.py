import heapq
from typing import Optional

from automation.task import Task


class TaskQueue:

    def __init__(self):
        self.tasks: list[tuple[int, object, Task]] = []

    def add(self, task: Task):

        heapq.heappush(
            self.tasks,
            (task.priority, task.created_at, task)
        )

    def next(self) -> Optional[Task]:

        if not self.tasks:
            return None

        return heapq.heappop(self.tasks)[2]

    def empty(self) -> bool:

        return len(self.tasks) == 0

    def count(self) -> int:

        return len(self.tasks)


queue = TaskQueue()