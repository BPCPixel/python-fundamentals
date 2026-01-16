"""
RAM Assignation simulation by Operating System.
Author: Lalo Téllez
"""

print(f'{"*" * 20} RAM Simulation {"*" * 20}')

# Ask the user for the size of RAM
bytes_tam = int(input('Type the size of RAM: '))

# User menu
out_option = None

while out_option != True:
    option = int(input(f'''
Enter an option
1. Create processes
2. Delete processes
3. Search processes
4. Visualize RAM processes
5. Exit
OPTION: '''))
    if option == 1:
        print(f'\nOPTION 1')
    elif option == 2:
        print(f'\nOPTION 2')
    elif option == 3:
        print(f'\nOPTION 3')
    elif option == 4:
        print(f'\nOPTION 4')
    elif option == 5:
        print(f'\nOPTION 5')
        out_option = True
    else:
        print('\nInvalid option, try again ...')