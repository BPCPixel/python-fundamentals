"""
This a program to practice my knowledge from the beginning to loops

Author: Lalo Téllez
"""
import random
print(f'{"=" * 20} Mega Practice {"=" * 20}')

# Input data
name =  input("Type your name: ").strip()
age = input("Type your age: ").strip()

# String to Integer
age = int(age)

adult = None

# Validating age
if 100 > age >= 18:
    adult = True
elif 0 < age < 18:
    adult = False

# Printing the result of the age
if adult == True:
    print(f"Hello, {name.title()}.\nYou're an adult.\n")
elif adult == False:
    print(f"Hello, {name.title()}.\nYou're not an adult.\n")
else:
    print('Invalid age.\n')

valid_number = False

# Validating a number
while valid_number == False:
    number = int(input('Type a number between 1 and 10: '))
    if 1 <= number <= 10:
        valid_number = True

# Printing * number times
for i in range(number):
    print("*", end="")

print('\n')

# Creating a list
scores = [10, 20, 30]

# Adding the value that the user entered to the list
scores.append(number)

# Adding the number 99 to the second position
scores.insert(1, 99)

print(scores)

# Picking a random number
RANDOM_NUMBER = random.randint(1, 10)

guess = input('Do you want to guess what the random number is (yes/no)? ').strip().lower()

if guess == 'yes':
    guess = True
    correct = False
    
    while correct == False:
        user_number = int(input('Guess the number between 1 and 10: '))
        
        if user_number == RANDOM_NUMBER:
            correct = True
            print(f'Correct! The random number was {RANDOM_NUMBER}\n')
        else:
            print('Wrong number, try again.')
    
elif guess == 'no':
    guess = False
else:
    guess = None

print(f'Goodbye, {name.title()}\n')

print(f'{"=" * 50}')
