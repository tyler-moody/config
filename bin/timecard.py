#!/usr/bin/python3

import argparse
import datetime
import os
import sys
import yaml

def config_value(field):
    config_file = open(os.path.expanduser('~/.timecard'),'r')
    config = yaml.load(config_file)
    return config[field]

def summarize(date):
    print('a summary of week starting {} goes here'.format(date))

def current_timecard_filename():
    today = datetime.datetime.today()
    monday = datetime.date.fromordinal(today.toordinal() - today.weekday())
    filename = monday.strftime('%Y-%m-%d')
    directory = os.path.expanduser(config_value('directory'))
    return os.path.join(directory, filename)

def add_record(task, timestamp, description):
    line = '{}:::{}:::{}\n'.format(timestamp, task, description)
    with open(current_timecard_filename(), 'a') as f:
        f.write(line)

def parse_arguments(args):
    if len(args) < 2:
        exit(1)
    first = args[1]
    if first == 'summary':
        if len(args) > 2:
            date = args[2]
        else:
            today = datetime.datetime.today()
            monday = datetime.date.fromordinal(today.toordinal() - today.weekday())
            date = monday
        summarize(date)
    elif first == 'manual':
        timestamp = datetime.datetime.strptime(args[2], '%Y%m%d_%H:%M')
        task = args[3]
        description = ' '.join(args[4:])
        add_record(task, timestamp, description)

    else:
        task = args[1]
        timestamp = datetime.datetime.now()
        description = ' '.join(args[2:])
        add_record(task, timestamp, description)

if __name__ == '__main__':
    parse_arguments(sys.argv)
