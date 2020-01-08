students = []

# constructor method in python is call __init__


class Student:

    school_name = 'Rainier Valley High'
    extracurricular = 'none'

    def __init__(self, name, student_id=3407786074):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student: " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

    def get_extracurricular(self):
        return self.extracurricular
