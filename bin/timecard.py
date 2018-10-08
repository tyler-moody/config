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

def sum_time_by_task(records):
    # collect accumulated time, descriptions for each task
    tasks = {}
    for r in records:
        task = r['task']
        duration = minutes(r['duration'])
        description = r['description']
        if task in tasks:
            tasks[task]['duration'] += duration
            tasks[task]['description'] += ', ' + description
        else:
            tasks[task] = {'duration': duration, 'description': description}
    for t in tasks:
        tasks[t]['duration'] = duration_fmt(tasks[t]['duration'])
    return tasks

def calc_total_minutes(records):
    total_minutes = 0
    for r in records:
        duration = minutes(r['duration'])
        total_minutes += duration
    return total_minutes

_format_spec = '{:20s}\t{:8s}\t{}'
def print_tasks(tasks):
    print(_format_spec.format('TASK', 'DURATION', 'DESCRIPTION'))
    for t in tasks:
        print(_format_spec.format(t, tasks[t]['duration'], tasks[t]['description']))

def print_total(total_minutes):
    print(_format_spec.format(20*'-', 8*'-',''))
    print(_format_spec.format('total time', duration_fmt(total_minutes),''))

def summarize_week(monday):
    records = list()
    for d in [monday + datetime.timedelta(days=n) for n in range(5)]:
        records += get_records(d)
    print('summary for week starting {}'.format(monday.strftime('%Y-%m-%d')))
    print_tasks(sum_time_by_task(records))
    print_total(calc_total_minutes(records))

def summarize_day(date):
    records = get_records(date)
    print('summary for {}:'.format(date.strftime('%Y-%m-%d')))
    print_tasks(sum_time_by_task(records))
    print_total(calc_total_minutes(records))

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
        summarize_day(today)
    elif first == 'yesterday':
        today = datetime.datetime.today()
        last_workday = today - datetime.timedelta(days=1)
        while last_workday.weekday() > 4:
            last_workday -= datetime.timedelta(days=1)
        summarize_day(last_workday)
    elif first == 'week':
        today = datetime.datetime.today()
        # find the previous monday (back up 1 week if today is monday)
        last_monday = today - datetime.timedelta(days=1)
        while last_monday.weekday() != 0:
            last_monday = last_monday - datetime.timedelta(days=1)
        summarize_week(last_monday)
    else:
        today = datetime.datetime.today()
        task = args[1]
        duration = args[2]
        description = ' '.join(args[3:])
        add_record(today, duration, task, description)

if __name__ == '__main__':
    parse_arguments(sys.argv)
