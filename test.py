from tasks import CompositeTask, Task
from todo_list import TodoList


task2 = Task("Task 2")
task3 = Task("Task 3")
task_compo = CompositeTask("Task 1")
task_compo.add_task(task2)
task_compo.add_task(task3)
task_compo.mark_complete()
todolist = TodoList()
todolist.add_task(task_compo)
todolist.display_tasks()