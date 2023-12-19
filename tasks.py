from interfaces import ITask


class Task(ITask):
    def get_detail(self):
        status = "Completed" if self.completed else "Pending"
        return f"Task: {self.name}, Status: {status}"


class CompositeTask(ITask):

    def __init__(self, name: str):
        super().__init__(name)
        self.subtasks: list[ITask] = []

    def add_subtask(self, subtask:ITask):
        self.subtasks.append(subtask)

    def get_detail(self):
        status = "Completed" if self.completed else "Pending"
        details = [f"Composite Task: {self.name}, Status: {status}\n\tSubtasks:"]

        for subtask in self.subtasks:
            details.append("\t- " + subtask.get_detail())

        return "\n".join(details)

    def mark_complete(self):
        self.completed = True
        if self.completed:
            for subtask in self.subtasks:
                subtask.completed = True