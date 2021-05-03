import pytest
from pathlib import Path

from todos import TaskManager, SQLiteRepository


@pytest.fixture
def task_manager():
    sqlite_path = Path("tests.db")
    repository = SQLiteRepository(sqlite_path)
    repository.clean()
    task_manager = TaskManager()
    task_manager.set_repository(repository)
    return task_manager
