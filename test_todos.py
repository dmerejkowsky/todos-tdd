from todos import AddAction, DeleteAction, Task, TaskManager, UpdateAction, parse


def test_can_create_an_add_action():
    add_action = AddAction(description="new task")

    assert add_action.description == "new task"


def test_can_create_an_update_action():
    set_as_done_action = UpdateAction(number=1, done=True)

    assert set_as_done_action.number == 1
    assert set_as_done_action.done == True


def test_can_create_a_delete_action():
    delete_one_action = DeleteAction(number=1)

    assert delete_one_action.number == 1


def test_can_instantiate_a_task():
    new_task = Task(number=1, description="new task", done=False)

    assert new_task.number == 1
    assert new_task.description == "new task"
    assert new_task.done is False


def test_can_parse_add_command():
    cmd = "+ other task"

    action = parse(cmd)

    assert isinstance(action, AddAction)
    assert action.description == "other task"


def test_can_parse_set_done_command():
    cmd = "x 1"

    action = parse(cmd)

    assert isinstance(action, UpdateAction)
    assert action.number == 1
    assert action.done is True


def test_can_parse_set_not_done_command():
    cmd = "o 2"

    action = parse(cmd)

    assert isinstance(action, UpdateAction)
    assert action.number == 2
    assert action.done is False


def test_task_manager_has_no_tasks_by_default():
    task_manager = TaskManager()

    assert task_manager.tasks == []


def test_execute_add_action():
    task_manager = TaskManager()
    add_action = AddAction(description="new task")

    task_manager.execute(add_action)

    (actual,) = task_manager.tasks
    assert actual.description == "new task"
    assert actual.number == 1


def test_execute_update_action():
    """Scenario:

    * Create a TaskManager with one task('task one') that is not done
    * Create an UpdateAction(number=1, done=True)

    * Call task_manager.execute()

    * Check that action number 1 is now done
    """
    task_manager = TaskManager()
    task_manager.tasks = [Task(number=1, description="task one", done=False)]
    update_action = UpdateAction(number=1, done=True)

    task_manager.execute(update_action)

    (actual,) = task_manager.tasks
    assert actual.done is True


def test_execute_delete_action():
    """Scenario:

    * Create a TaskManager with one task('task one') that is not done
    * Create an DeleteAction(number=1)

    * Call task_manager.execute()

    * Check that tasks list is empty
    """
    task_manager = TaskManager()
    task_manager.tasks = [Task(number=1, description="task one", done=False)]
    delete_action = DeleteAction(number=1)

    task_manager.execute(delete_action)

    assert not task_manager.tasks
