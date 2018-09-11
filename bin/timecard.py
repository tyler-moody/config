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

def minutes(duration):
    if 'h' in duration:
        (hours, duration) = duration.split('h')
        hours = int(hours)
    else:
        hours = 0
    if 'm' in duration:
        (minutes, duration) = duration.split('m')
        minutes = int(minutes)
    else:
        minutes = 0
    return (60*hours + minutes)

def duration_fmt(minutes):
    hours = minutes // 60
    minutes -= hours*60
    return '{}h{}m'.format(hours, minutes)


def summarize(date):
    print('summary for {}:'.format(date.strftime('%Y-%m-%d')))
    records = get_records(date)

    # collect accumulated time, descriptions for each task
    tasks = {}
    total_minutes = 0
    for r in records:
        task = r['task']
        duration = minutes(r['duration'])
        total_minutes += duration
        description = r['description']
        if task in tasks:
            tasks[task]['duration'] += duration
            tasks[task]['description'] += ', ' + description
        else:
            tasks[task] = {'duration': duration, 'description': description}
    for t in tasks:
        tasks[t]['duration'] = duration_fmt(tasks[t]['duration'])

    format_spec = '{:20s}\t{:8s}\t{}'
    print(format_spec.format('TASK', 'DURATION', 'DESCRIPTION'))
    for t in tasks:
        print(format_spec.format(t, tasks[t]['duration'], tasks[t]['description']))
    print(format_spec.format(20*'-', 8*'-',''))
    print(format_spec.format('total time', duration_fmt(total_minutes),''))

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
