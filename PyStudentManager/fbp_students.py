from student import Student


class HighschoolFootballPlayer(Student):
    extracurricular = "Football Player"

    def get_extracurricular(self):
        return 'This is a football player'

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + ' is a HS Football Player'
