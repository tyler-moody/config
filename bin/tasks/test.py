from task import TaskApp
import unittest

class TestTaskApp(unittest.TestCase):
    def setUp(self):
        self.tasks = TaskApp()
        pass

    def tearDown(self):
        pass

    def test_create(self):
        pass

if __name__ == '__main__':
    unittest.main()
