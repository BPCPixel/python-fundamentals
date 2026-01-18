"""
RAM Assignation simulation by Operating System.
Author: Lalo Téllez
"""
import random

print(f'{"*" * 20} RAM Simulation {"*" * 20}')



automatic_PID = 0

out_option = None

automatic_state = None

process_name = f'No Name Yet'
process_size = 0

name_list_increment = 0
name_list = []

# User menu
while out_option != True:
    option = int(input(f'''
{"-" * 5} USER MENU {"-" * 5}
Enter an option
1. Create processes
2. Delete processes
3. Search processes
4. Visualize RAM processes
5. Exit
OPTION: '''))

    if option == 1:

        print(f'\n{"-" * 5}Crating processes {"-" * 5}')
        
        process_name = input('Type the name of the procces: ')
        
        if process_name in (name_list):
            print('You should pick another name: ')
        else:  
            name_list.insert(name_list_increment, process_name)
            name_list_increment += 1
            
        process_size = int(input('Type the size of the procces: '))
        automatic_PID += 1
        random_value = random.randint(1,3)

        if random_value == 1:
            automatic_state = f'READY\n'
        elif automatic_state == 2:
            automatic_state = f'EXECUTE\n'
        else:
            automatic_state = f'WAIT\n'
        bytes_size = int(input('Type the size of RAM: '))
        
    elif option == 2:
        print(f'\nOPTION 2')
    elif option == 3:
        print(f'\nOPTION 3')
        
    elif option == 4:
        print(f'\n{"-" * 5} Visualize RAM processes {"-" * 5}')
        
        print(f'''RAM:
PID: {automatic_PID}
Proccess Name: {process_name}
Size of the progress: {process_size}
STATE: {automatic_state}''')
    
    elif option == 5:
        print(f'\nOPTION 5')
        out_option = True
    else:
        print('\nInvalid option, try again ...')