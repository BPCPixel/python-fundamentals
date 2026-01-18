"""
This code demonstrates how to iterate through a list.

Author: Lalo Téllez
"""

print(f'{"=" * 20} Iterating a List {"=" * 20}\n')

names = ["Chris", "Cynthia", "Domi"]
print('Names List:')
for name in names:
    print(name)

print('\nHeterogeneous List:')
heterogeneous_list = [100, True, "Evelin"]
for element in heterogeneous_list:
    print(element)

print(f'\n{"=" * 50}')
