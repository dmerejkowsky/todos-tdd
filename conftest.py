import pytest
from pathlib import Path

from todos import TaskManager


@pytest.fixture
def task_manager():
    sqlite_path = Path("tests.db")
    return TaskManager(sqlite_path)
