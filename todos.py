def main():
    task_manager = TaskManager()
    print(task_manager)
    while True:
        command = input(">>> ")
        if command == "quit":
            break
        action = parse(command)
        if not action:
            print("invalid command")
            continue
        task_manager.execute(action)
        print(task_manager)


class TaskManager:
    def __init__(self):
        self.tasks = []

    def execute(self, action):
        if isinstance(action, AddAction):
            self.execute_add(action)
        elif isinstance(action, UpdateAction):
            self.execute_update(action)
        elif isinstance(action, DeleteAction):
            self.execute_delete(action)

    def execute_add(self, action):
        description = action.description
        number = len(self.tasks) + 1
        task = Task(number=number, description=description, done=False)
        self.tasks.append(task)

    def execute_delete(self, action):
        number = action.number
        self.tasks = [t for t in self.tasks if t.number != number]

    def execute_update(self, action):
        number = action.number
        done = action.done
        task = self.find_task(number=number)
        task.done = done

    def find_task(self, *, number):
        for i, task in enumerate(self.tasks, start=1):
            if i == number:
                return task

    def __str__(self):
        if not self.tasks:
            return "Nothing to be done yet"
        return "\n".join(str(t) for t in self.tasks)


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


class AddAction:
    def __init__(self, *, description):
        self.description = description


class DeleteAction:
    def __init__(self, *, number):
        self.number = number


class UpdateAction:
    def __init__(self, *, number, done):
        self.number = number
        self.done = done


class Task:
    def __init__(self, *, number, description, done):
        self.number = number
        self.description = description
        self.done = done

    def __str__(self):
        box = "[x]" if self.done else "[ ]"
        return f"{self.number} {box} {self.description}"


def extract_argument(cmd):
    return cmd[2:]


if __name__ == "__main__":
    main()
