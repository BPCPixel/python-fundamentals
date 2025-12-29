# This code simulates a system where it transforms a numeric grade to an alphabetical grade

print(f'{"=" * 20} Grading System {"=" * 20}\n')

# User input
numeric_grade = float(input('Enter your grade between 0 - 10: '))

# Assign a numerical grade to an alphabetical grade
grade = None

if 0 <= numeric_grade <= 10:
    if numeric_grade >= 9:
        grade = 'A'
    elif numeric_grade >= 8:
        grade = 'B'
    elif numeric_grade >= 7:
        grade = 'C'
    elif numeric_grade >= 6:
        grade = 'D'
    else:
        grade = 'F'

# Output
if grade:
    print(f'Your grade is {grade}')
else:
    print('Invalid grade. Please enter a value between 0 and 10.')
    
print(f'\n{"=" * 50}')