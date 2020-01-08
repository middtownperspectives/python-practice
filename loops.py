student_names = ['james', 'Katarina', 'Jessica',
                 'Mark', 'Bort', 'Rick Grimes', 'Max Power']

for name in student_names:
    if name == "Rick Grimes":
        print('Found him! ' + name)
        break
    print('Currently testing ' + name)

for name in student_names:
    if name == "Bort":
        continue
    print('Currently testing ' + name)
