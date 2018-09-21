#!/usr/bin/python3
"""A task tracking application"""

from datetime import datetime
from os import listdir
from os import path
from yaml import load, dump

class TaskApp():
    """The application"""
    def __init__(self):
        self.record_directory = ''
        self._projects = []

    def set_record_directory(self, directory):
        """Assigns the directory to read/write projects from/to"""
        self.record_directory = directory

    def load_projects(self) -> bool:
        """Loads all projects in the record directory"""
        projects_directory = path.join(self.record_directory, 'projects')
        if path.isdir(projects_directory):
            for proj_name in listdir(projects_directory):
                if path.isdir(path.join(projects_directory, proj_name)):
                    self._projects.append(proj_name)
            directory_exists = True
        else:
            directory_exists = False
        return directory_exists

    def _get_project_directory(self, project_name) -> str:
        """Returns the current project directory"""
        directory = path.join(self.record_directory, 'projects', project_name)
        return directory

    def create_project(self, project_name) -> bool:
        """Creates a new project"""
        already_exists = any([proj.name == project_name for proj in self._projects])
        if not already_exists:
            self._projects.append(Project(project_name))
        return not already_exists

class Project():
    """Represents a desired outcome with more than one action"""
    def __init__(self, name):
        """Creates a project"""
        self.name = name
        self.actions = []

    def add_action(self, action):
        """Adds an action to the Project"""
        self.actions.append(action)

    def write_to_file(self, filename):
        """Writes a project to a file"""
        record = dict()
        record['name'] = self.name
        record['actions'] = list()
        for action in self.actions:
            record['actions'].append(action.to_dict())
        with open(filename, 'w') as stream:
            dump(record, stream)

    @staticmethod
    def from_file(filename):
        """Creates a Project from a file"""
        with open(filename, 'r') as stream:
            record = load(stream)
            project = Project(name=record['name'])
            for action in record['actions']:
                project.add_action(Action.from_dict(action))
        return project

    def __eq__(self, other):
        """Returns True if the instances are equal"""
        return (self.__dict__ == other.__dict__) if isinstance(other, self.__class__) else False

class Action():
    """Represents a single to-do action"""
    def __init__(self, description, start=datetime.today(), due=datetime.today(), notes=''):
        """Initializes an Action"""
        self.start = start
        self.due = due
        self.description = description
        self.notes = notes

    def to_dict(self):
        """Creates a dict record from an Action"""
        record = dict()
        record['description'] = self.description
        record['due'] = self.due.timestamp()
        record['start'] = self.start.timestamp()
        record['notes'] = self.notes
        return record

    @staticmethod
    def from_dict(record):
        """Creates an Action from a dict"""
        action = Action(record['description'])
        action.start = datetime.fromtimestamp(record['start'])
        action.due = datetime.fromtimestamp(record['due'])
        action.notes = record['notes']
        return action

    def __eq__(self, other):
        """Returns True if the instances are equal"""
        return (self.__dict__ == other.__dict__) if isinstance(other, self.__class__) else False

if __name__ == '__main__':
    print('main running')
