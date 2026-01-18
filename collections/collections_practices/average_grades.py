"""
Practice: Program that asks a student for their grades and prints the average grade.

Author: Lalo Téllez
"""

print(f'{"=" * 20} Average Grades {"=" * 20}\n')

grades_number = int(input('Number of grades: '))
grades_list = []

# Iterating through the grades
for i in range(grades_number):
    grade = float(input(f'Grade[{i + 1}] = '))
    grades_list.append(grade)

# Printing grades
print(f'\nGrades: {grades_list}')

# Calculating the average grade
total = sum(grades_list)
average = total / grades_number

print(f'Average Grade: {average:.2f}')

print(f'\n{"=" * 50}')
