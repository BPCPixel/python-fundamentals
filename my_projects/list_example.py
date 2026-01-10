"""
Practice: This is a code where I put in practice what I've learned about lists.

Author: Lalo Téllez
"""

print(f'{"=" * 20} List Example {"=" * 20}')

# User input
name = input('Enter your name: ')
age = input('Enter your age: ')
fruit = input('Enter your favorite fruit: ')

# Normalize user info
normalized_name = name.strip().title()
normalized_fruit = fruit.strip().title()
age = int(age)

# Building a data list
data = [normalized_name, age, normalized_fruit]
print(f'\n{data} -> Initial List\n')

print(f'''{"-" * 10} DATA {"-" * 10}

First element: {data[0]}
Last element: {data[-1]}
Penultimate element: {data[-2]}\n''')

# Adding 5 years to age
increase_age = age + 5
print(f'Modified age: {increase_age}\n')

# Updating data
data[1] = increase_age

# Adding a new element at the end of the list
data.append('Python')
print(f'{data} -> A new element was added with append')

# Adding a new element at the first index
data.insert(1, 'New')
print(f'{data} -> A new element was added at the first index\n')

# Length of the list
length_list = len(data)
print(f'Final length of the list: {length_list}\n')

print(f'{"=" * 50}')
