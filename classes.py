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

# robinson = Student('Jackie robinson', 24)
# print(robinson)


print(Student.school_name)


class HighschoolFootballPlayer(Student):
    extracurricular = "Football Player"

    def get_extracurricular(self):
        return 'This is a football player'

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + ' is a HS Football Player'


oscar = HighschoolFootballPlayer('oscar')
print(oscar.get_name_capitalize())
