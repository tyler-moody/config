"""tests for the TaskApp class and its support classes"""

import unittest
from datetime import datetime
from os import mkdir, path, remove
from shutil import rmtree
from task import Action, Project, TaskApp

def create_clean_directory(directory):
    """creates an empty directory for tests that read/write files"""
    if path.exists(directory):
        rmtree(directory)
    mkdir(directory)

class TestTaskApp(unittest.TestCase):
    """tests for the TaskApp class"""
    def setUp(self):
        """prepare for a test"""
        self.directory = 'test_resources'
        create_clean_directory(self.directory)
        self.task_app = TaskApp()
        self.task_app.set_record_directory(self.directory)


    def tearDown(self):
        """clean up after a test"""
        rmtree(self.directory)

    def test_create(self):
        """test for instance creation"""
        pass

    def test_create_project(self):
        """test for the create_project method"""
        name = 'project'
        self.task_app.create_project(name)
        self.assertEqual(1, sum([proj.name == name for proj in self.task_app._projects]))

    def test_fail_to_create_duplicate_projects(self):
        """ensure that the app won't allow two projects with the same name"""
        name = 'project'
        self.assertTrue(self.task_app.create_project(name))
        self.assertEqual(1, sum([proj.name == name for proj in self.task_app._projects]))
        self.assertFalse(self.task_app.create_project(name))
        self.assertEqual(1, sum([proj.name == name for proj in self.task_app._projects]))

class TestProject(unittest.TestCase):
    """tests for the Project class"""
    def setUp(self):
        """prepare for a test"""
        self.project = Project(name='proj')
        self.directory = 'test_resources'
        create_clean_directory(self.directory)

    def tearDown(self):
        """clean up after a test"""
        rmtree(self.directory)

    def test_create(self):
        """test for instance creation"""
        self.assertEqual('proj', self.project.name)
        self.assertEqual(0, len(self.project.actions))

    def test_add_action(self):
        """test for add_action method"""
        action = Action(description='foo')
        self.project.add_action(action)
        self.assertEqual(action, self.project.actions[0])

    def test_write_to_file(self):
        """test for to_file method"""
        filename = path.join('test_resources', 'test_project.yaml')
        if path.exists(filename):
            remove(filename)

        self.project.add_action(Action(description='foo'))
        self.project.add_action(Action(description='bar'))

        self.project.write_to_file(filename)

    def test_equal_names(self):
        """test for __eq__ method"""
        project = Project(name='foo')
        other = Project(name='foo')
        self.assertEqual(project, other)
        other.name = 'bar'
        self.assertNotEqual(project, other)

    def test_equal_actions(self):
        """test for __eq__ method"""
        project = Project(name='foo')
        other = Project(name='foo')
        action = Action(description='f')
        project.add_action(action)
        self.assertNotEqual(project, other)
        other.add_action(action)
        self.assertEqual(project, other)

    def test_read_from_file(self):
        """test for from_file method"""
        filename = path.join('test_resources', 'test_project.yaml')
        if path.exists(filename):
            remove(filename)

        action = Action(description='foo')
        self.project.add_action(action)
        self.project.write_to_file(filename)

        copy = Project.from_file(filename)
        self.assertEqual(self.project, copy)

class TestAction(unittest.TestCase):
    """tests for the Action class"""
    def setUp(self):
        """prepare for a test"""
        pass

    def tearDown(self):
        """clean up a test"""
        pass

    def test_create(self):
        """test for instance creation"""
        action = Action(description='')

    def test_to_from_record(self):
        """test for to_record and from_record methods"""
        action = Action(description='foo',
                        start=datetime.today(),
                        due=datetime(year=2020, month=2, day=28),
                        notes='bar')
        other = Action.from_dict(action.to_dict())
        self.assertEqual(action, other)

    def test_eq(self):
        """test for __eq__ method"""
        action = Action(description='foo')
        other = Action(description='foo')
        self.assertEqual(action, other)
        other.description = 'bar'
        self.assertNotEqual(action, other)

if __name__ == '__main__':
    unittest.main()
