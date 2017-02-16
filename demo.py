"""This script demonstrates the usage of our scheduler for the problem given in the lecture.
"""
from scheduler import Timetable
from scheduler.exceptions import ImpossibleAssignments

# name
lecture_list = [
    'Lecture 1',
    'Lecture 2',
    'Lecture 3',
    'Lecture 4',
    'Lecture 5',
    'Lecture 6',
    'Lecture 7',
    'Lecture 8',
    'Lecture 9',
    'Lecture 10',
    'Lecture 11',
    'Lecture 12',
    'Lecture 13',
    'Lecture 14',
    'Lecture 15',
    'Lecture 16',
    'Lecture 17',
    'Lecture 18',
    'Lecture 19',
    'Lecture 20',
]

# name lectures[] days[] times[]
instructor_list = [
    ['1', ['Lecture 1',
            'Lecture 2',
            'Lecture 3',
            'Lecture 4',
            'Lecture 5',], ['Tue', 'Wed', 'Thu'], []],
    ['2', ['Lecture 1',
            'Lecture 2',
            'Lecture 3',
            'Lecture 4',
            'Lecture 5',
            'Lecture 11',
            'Lecture 12',
            'Lecture 13',
            'Lecture 14',
            'Lecture 15',], ['Mon', 'Tue', 'Wed'], []],
    ['3', ['Lecture 6',
            'Lecture 7',
            'Lecture 8',
            'Lecture 9',
            'Lecture 10',
            'Lecture 16',
            'Lecture 17',
            'Lecture 18',
            'Lecture 19',
            'Lecture 20',], ['Thu', 'Fri'], []],
    ['4', ['Lecture 6',
            'Lecture 7',
            'Lecture 8',
            'Lecture 9',
            'Lecture 10',], [], ['10-12', '12-14']],
    ['5', ['Lecture 11',
            'Lecture 12',
            'Lecture 13',
            'Lecture 14',
            'Lecture 15',
            'Lecture 16',
            'Lecture 17',
            'Lecture 18',
            'Lecture 19',
            'Lecture 20',], [], ['8-10', '10-12']],
]

# number lectures[] days[] times[]
room_list = [
    [1, ['Lecture 1',
        'Lecture 2',
        'Lecture 3',
        'Lecture 4',
        'Lecture 5',
        'Lecture 6',
        'Lecture 7',
        'Lecture 8',
        'Lecture 9',
        'Lecture 10',
        'Lecture 11',
        'Lecture 12',
        'Lecture 13',
        'Lecture 14',
        'Lecture 15',
        'Lecture 16',
        'Lecture 17',
        'Lecture 18',
        'Lecture 19',
        'Lecture 20',], ['Mon'], []],
    [2, ['Lecture 1',
        'Lecture 2',
        'Lecture 3',
        'Lecture 4',
        'Lecture 5',
        'Lecture 6',
        'Lecture 7',
        'Lecture 8',
        'Lecture 9',
        'Lecture 10',], ['Mon', 'Tue', 'Wed', 'Thu'], []],
    [3, ['Lecture 11',
        'Lecture 12',
        'Lecture 13',
        'Lecture 14',
        'Lecture 15',
        'Lecture 16',
        'Lecture 17',
        'Lecture 18',
        'Lecture 19',
        'Lecture 20',], ['Tue', 'Wed', 'Thu', 'Fri'], []],
    [4, ['Lecture 1',
        'Lecture 2',
        'Lecture 3',
        'Lecture 4',
        'Lecture 5',
        'Lecture 6',
        'Lecture 7',
        'Lecture 8',
        'Lecture 9',
        'Lecture 10',], [], ['8-10']],
    [5, ['Lecture 11',
        'Lecture 12',
        'Lecture 13',
        'Lecture 14',
        'Lecture 15',
        'Lecture 16',
        'Lecture 17',
        'Lecture 18',
        'Lecture 19',
        'Lecture 20',], [], ['12-14']],
]
# day start-end
timeslot_list = [
    'Mon 8-10',
    'Mon 10-12',
    'Mon 12-14',
    'Tue 8-10',
    'Tue 10-12',
    'Tue 12-14',
    'Wed 8-10',
    'Wed 10-12',
    'Wed 12-14',
    'Thu 8-10',
    'Thu 10-12',
    'Thu 12-14',
    'Fri 8-10',
    'Fri 10-12',
    'Fri 12-14',
]

timetable = Timetable(lecture_list, instructor_list, room_list, timeslot_list,
                      max_lectures_per_instructor=5)

try:
    timetable.find_schedule()
    print(timetable)
except ImpossibleAssignments as e:
    print(e)
    
    
    