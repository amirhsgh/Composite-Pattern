from interfaces import ITask


class TodoList:
    def __init__(self):
        self.tasks: list[ITask] = []

    def add_task(self, task: ITask):
        self.tasks.append(task)

    def display_tasks(self):
        for task in self.tasks:
            task.display()
