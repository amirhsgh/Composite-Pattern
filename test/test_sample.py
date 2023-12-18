import unittest
from tasks import Task, CompositeTask


def normalize_string(s):
    return ' '.join(s.lower().split())


class TestTask(unittest.TestCase):
    def assertEqualNormalized(self, a, b):
        self.assertEqual(normalize_string(a), normalize_string(b))

    def test_task_initialization(self):
        task = Task("Test Task")
        self.assertEqualNormalized(task.name, "test task")
        self.assertFalse(task.completed)
