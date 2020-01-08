# python dictionaries are very similar to JSON
student = {
    'name': 'Mark',
    'student_id': 15163,
    'feedback': None
}

all_students = [
    {
        'name': 'Mark',
        'student_id': 15163,
        'feedback': None
    },
    {
        'name': 'Katrina',
        'student_id': 63112,
        'feedback': 'Amazingly talented Designer'
    },
    {
        'name': 'Jessica',
        'student_id': 30021,
        'feedback': None
    }
]

print(student.keys())
print(student.values())

student['last_name'] = 'Kawasaki'
# exception handleing
try:
    last_name = student['last_name']
    numbered_last_name = 3 + last_name
except KeyError:
    print('Error finding last_name')
except TypeError as error:
    print('This is not my type')
    print(error)

print('This code executed!')
