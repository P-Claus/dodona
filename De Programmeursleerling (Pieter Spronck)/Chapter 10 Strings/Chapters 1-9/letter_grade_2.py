# read numeric grade
numeric_grade = int(input())

# determine corresponding letter grade
if numeric_grade >= 90:
    letter_grade = 'A'
elif numeric_grade >= 80:
    letter_grade = 'B'
elif numeric_grade >= 70:
    letter_grade = 'C'
elif numeric_grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# print corresponding letter grade
print(letter_grade)
