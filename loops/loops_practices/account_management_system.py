"""
Practice: Account Management System

The objective of this practice is to learn how to create an interactive menu
and how the optional else clause for while works.

Author: Lalo Tellez
"""

print(f'{"=" * 20} Account Management System {"=" * 20}\n')

# Control variable for the system loop
exit_system = False

while not exit_system:
    print(f'''Menu:
    1. Create an account
    2. Delete account
    3. Exit''')
    
    option = int(input('Select an option: '))

    if option == 1:
        print('Creating an account\n')
    elif option == 2:
        print('Deleting account\n')
    elif option == 3:
        print('Closing system...\n')
        exit_system = True
    else:
        print('Invalid Option, try again.\n')
else:
    # This executes when the while loop finishes normally
    print('Finishing account management system')
    
print(f'{"=" * 50}')
