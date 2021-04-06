import pytest

from todos import TaskManager

@pytest.fixture
def task_manager(tmp_path):
    pickle_path = tmp_path / "tasks.pickle"
    return TaskManager(pickle_path)
