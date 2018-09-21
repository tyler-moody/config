from datetime import datetime
from os import path, remove
from shutil import rmtree
from task import Action, Project, TaskApp
import unittest

class TestTaskApp(unittest.TestCase):
    def setUp(self):
        self.directory = 'test_resources/'
        self.tasks = TaskApp()
        self.tasks.set_record_directory(self.directory)
        pass

    def tearDown(self):
        pass

    def test_create(self):
        pass

    def test_setRecordDirectory(self):
        self.assertEqual(self.directory, self.tasks.record_directory)

    def test_loadProjectsSuccess(self):
        self.assertTrue(self.tasks.load_projects())
        projects = ['Proj0', 'Proj1', 'Proj2']
        for p in projects:
            self.assertTrue(p in self.tasks.projects)

    def test_loadProjectsFailure(self):
        self.tasks.set_record_directory('foo')
        self.assertFalse(self.tasks.load_projects())

    def test_createProject(self):
        new_project_name = 'NewProj'
        new_project_dir = path.join(self.directory, 'projects', new_project_name)
        if path.exists(new_project_dir):
            rmtree(new_project_dir)
        self.assertTrue(self.tasks.create_project(new_project_name))
        self.assertTrue(path.exists(path.join(self.directory, 'projects', new_project_name)))

    def test_FailToCreateDuplicateProject(self):
        new_project_name = 'NewProj'
        new_project_dir = path.join(self.directory, 'projects', new_project_name)
        if path.exists(new_project_dir):
            rmtree(new_project_dir)
        self.assertTrue(self.tasks.create_project(new_project_name))
        self.assertFalse(self.tasks.create_project(new_project_name))

class TestProject(unittest.TestCase):
    def setUp(self):
        self.project = Project(name='proj')

    def tearDown(self):
        pass

    def test_Create(self):
        self.assertEqual('proj', self.project.name)
        self.assertEqual(0, len(self.project.actions))

    def test_AddAction(self):
        action = Action(description='foo')
        self.project.add_action(action)
        self.assertEqual(action, self.project.actions[0])

    def test_writeToFile(self):
        filename = path.join('test_resources', 'test_project.yaml')
        if path.exists(filename):
            remove(filename)

        a0 = Action(description = 'foo')
        self.project.add_action(a0)
        a1 = Action(description = 'bar')
        self.project.add_action(a1)

        self.project.write_to_file(filename)

    def test_equalNames(self):
        a = Project(name='foo')
        b = Project(name='foo')
        self.assertEqual(a,b)
        b.name = 'bar'
        self.assertNotEqual(a,b)

    def test_equalActions(self):
        a = Project(name='foo')
        b = Project(name='foo')
        a0 = Action(description='f')
        a.add_action(a0)
        self.assertNotEqual(a,b)
        b.add_action(a0)
        self.assertEqual(a,b)

    def test_readFromFile(self):
        filename = path.join('test_resources', 'test_project.yaml')
        if path.exists(filename):
            remove(filename)

        a = Action(description = 'foo')
        self.project.add_action(a)
        self.project.write_to_file(filename)

        projCopy = Project.from_file(filename)
        self.assertEqual(self.project, projCopy)

class TestAction(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Create(self):
        a = Action(description = '')

    def test_toFromRecord(self):
        a = Action(description='foo', 
                start = datetime.today(),
                due = datetime(year=2020, month=2, day=28),
                notes = 'bar'
            )
        b = Action.from_dict(a.to_dict())
        self.assertEqual(a,b)

    def test_Equality(self):
        a = Action(description='foo')
        b = Action(description='foo')
        self.assertEqual(a,b)
        b.description = 'bar'
        self.assertNotEqual(a,b)

if __name__ == '__main__':
    unittest.main()
