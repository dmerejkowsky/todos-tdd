import pytest
from pathlib import Path

from todos import TaskManager


@pytest.fixture
def task_manager():
    sqlite_path = Path("tests.db")
    task_manager = TaskManager(sqlite_path)
    task_manager.repository.clean()
    return task_manager
