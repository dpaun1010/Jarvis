import time

from automation.queue import queue
from automation.task import Task


class Scheduler:

    def start(self):

        while not queue.empty():

            task: Task = queue.next()

            if task is None:
                break

            task.status = "RUNNING"

            try:

                if task.delay > 0:
                    time.sleep(task.delay)

                task.action()

                task.status = "COMPLETED"

            except Exception as e:

                print(f"Task '{task.name}' failed: {e}")

                task.status = "FAILED"

                if task.retries > 0:

                    task.retries -= 1

                    queue.add(task)


scheduler = Scheduler()