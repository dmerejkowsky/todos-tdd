from dataclasses import dataclass
from pathlib import Path

import sqlite3


def main():
    db_path = Path("tasks.db")
    repository = SQLiteRepository(db_path)
    task_manager = TaskManager()
    task_manager.set_repository(repository)
    task_manager.load_tasks()
    print(task_manager)
    while True:
        command = input(">>> ")
        if command in ("quit", "q"):
            break
        action = parse(command)
        if not action:
            print("invalid command")
            continue
        task_manager.execute(action)
        print(task_manager)


class SQLiteRepository:
    def __init__(self, path):
        self.path = path
        if not self.path.exists():
            connection = sqlite3.connect(self.path)
            with open("schema.sql") as f:
                connection.execute(f.read())
                connection.commit()

        self.connection = sqlite3.connect(self.path)
        self.connection.row_factory = sqlite3.Row

    def clean(self):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            DELETE FROM tasks
            """
        )
        self.connection.commit()

    def add_task(self, *, description):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            INSERT INTO tasks(description, done)
            VALUES (?, false)
        """,
            (description,),
        )
        self.connection.commit()

    def load_tasks(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT number, done, description FROM tasks")
        res = []
        for row in cursor.fetchall():
            task = Task(
                number=row["number"], done=row["done"], description=row["description"]
            )
            res.append(task)
        return res

    def delete_task(self, *, number):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM tasks WHERE number=?", (number,))
        self.connection.commit()

    def update_task(self, *, number, done):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE tasks SET done=? WHERE number=?", (done, number))
        self.connection.commit()


class TaskManager:
    def __init__(self):
        self.repository = None

    def set_repository(self, repository):
        self.repository = repository

    def load_tasks(self):
        return self.repository.load_tasks()

    def execute(self, action):
        if isinstance(action, AddAction):
            self.execute_add(action)
        elif isinstance(action, UpdateAction):
            self.execute_update(action)
        elif isinstance(action, DeleteAction):
            self.execute_delete(action)

    def execute_add(self, action):
        self.repository.add_task(description=action.description)

    def execute_delete(self, action):
        self.repository.add_task(number=action.number)

    def execute_update(self, action):
        self.repository.update_task(number=action.number, done=action.done)

    def __str__(self):
        tasks = self.load_tasks()
        if not tasks:
            return "Nothing to be done yet"
        return "\n".join(str(t) for t in tasks)


def parse(cmd):
    first_letter = cmd[0]
    argument = extract_argument(cmd)
    if first_letter == "+":
        return AddAction(description=argument)
    elif first_letter == "o":
        number = int(argument)
        return UpdateAction(number=number, done=False)
    elif first_letter == "x":
        number = int(argument)
        return UpdateAction(number=number, done=True)


@dataclass
class AddAction:
    description: str


@dataclass
class DeleteAction:
    number: int


@dataclass
class UpdateAction:
    number: int
    done: bool


class Task:
    def __init__(self, *, number, description, done):
        self.number = number
        self.description = description
        self.done = done

    def __str__(self):
        box = "[x]" if self.done else "[ ]"
        return f"{self.number} {box} {self.description}"

    def __repr__(self):
        return f"Task<#{self.number} - {self.description} done: {self.done}>"

    def __eq__(self, other):
        return (
            self.number == other.number
            and self.description == other.description
            and self.done == other.done
        )


def extract_argument(cmd):
    return cmd[2:]


if __name__ == "__main__":
    main()
