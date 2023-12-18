from abc import ABC, abstractmethod


class ITask(ABC):

    def __init__(self, name: str):
        self.name = name
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def display(self):
        print(self.get_detail())

    @abstractmethod
    def get_detail(self) -> str: ...
