#!/usr/bin/python3

import datetime
import os
from pathlib import Path
import sys
import yaml

def config_value(field):
    config_file = open(os.path.expanduser('~/.timecard'),'r')
    config = yaml.load(config_file)
    config_file.close()
    return config[field]

def get_records(date):
    if Path(timecard_filename(date)).is_file():
        with open(timecard_filename(date)) as f:
            records = yaml.load(f)
        return records
    else:
        return list()

def write_records(date, records):
    with open(timecard_filename(date), 'w') as f:
        yaml.dump(records, f, default_flow_style=False)

def summarize(date):
    print('summary for {}:'.format(date.strftime('%Y-%m-%d')))
    records = get_records(date)
    for r in records:
        print('task: {} \tduration: {} \tdescription: {}'.format(r['task'], r['duration'], r['description']))

def timecard_filename(date):
    filename = date.strftime('%Y-%m-%d')
    directory = os.path.expanduser(config_value('directory'))
    return os.path.join(directory, filename)

def add_record(date, duration, task, description):
    records = get_records(date)
    records.append({'duration': duration, 'task': task, 'description': description})
    write_records(date, records)

def parse_arguments(args):
    if len(args) < 2:
        args.append('today')
    first = args[1]
    if first in ['-h', '--help']:
        print('"timecard today" to get a summary of today\'s logged time')
        print('"timecard yesterday" to get a summary of the previous workday\'s logged time')
        print('"timecard <task> <duration> <description>" to add to today\'s logged time')
    elif first == 'today':
        today = datetime.datetime.today()
        summarize(today)
    elif first == 'yesterday':
        today = datetime.datetime.today()
        last_workday = today - datetime.timedelta(days=1)
        while last_workday.weekday() > 4:
            last_workday -= datetime.timedelta(days=1)
        summarize(last_workday)
    else:
        today = datetime.datetime.today()
        task = args[1]
        duration = args[2]
        description = ' '.join(args[3:])
        add_record(today, duration, task, description)

if __name__ == '__main__':
    parse_arguments(sys.argv)
