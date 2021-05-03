import pytest
from pathlib import Path

from todos import TaskManager, SQLiteRepository, Task


class FakeRepository:
    def __init__(self):
        self.tasks = []

    def clean(self):
        self.tasks = []

    def add_task(self, *, description):
        if not self.tasks:
            number = 1
        else:
            last = self.tasks[-1]
            number = last.number + 1
        new_task = Task(description=description, done=False, number=number)
        self.tasks.append(new_task)

    def load_tasks(self):
        return self.tasks

    def delete_task(self, *, number):
        self.tasks = [t for t in self.tasks if t.number != number]

    def update_task(self, *, number, done):
        for task in self.tasks:
            if task.number == number:
                task.done = done


@pytest.fixture
def task_manager():
    repository = FakeRepository()
    repository.clean()
    task_manager = TaskManager()
    task_manager.set_repository(repository)
    return task_manager
