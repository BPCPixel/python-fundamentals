"""
Practice: Create My First Calculator

This program is a calculator simulator where I practice loops.
The user selects an option, enters two values, and the program
continues running until the exit option is selected.

Author: Lalo Tellez
"""

print(f'{"=" * 20} Calculator in Python {"=" * 20}\n')

# Control variable for the main loop
is_running = True

while is_running:
    # Display calculator menu    
    print('''Operations you can perform: 
    1. Addition
    2. Substraction
    3. Multiplication
    4. Division
    5. Integer Division
    6. Exit''')
    option = int(input('Option: '))
    
    if 1 <= option <= 5:
        value_1 = float(input('\nEnter the first value: '))
        value_2 = float(input('Enter the second value: '))
    
        if option == 1:
            result = value_1 + value_2
        
            print(f'{value_1} + {value_2} = {result}\n')

        elif option == 2:
            result = value_1 - value_2
        
            print(f'{value_1} - {value_2} = {result:.2f}\n')
        
        elif option == 3:
            result = value_1 * value_2
        
            print(f'{value_1} * {value_2} = {result:.2f}\n')
        
        elif option == 4:
        
            if value_2 == 0:
                print('Error: Division by zero it not allowed\n')
            else:
                result = value_1 / value_2
                print(f'{value_1} / {value_2} = {result:.2f}\n')
        
        elif option == 5:
        
            if value_2 == 0:
                print('Error: Division by zero it not allowed\n')
            else:
                result = value_1 // value_2
                # Output with the answer
                print(f'{value_1} // {value_2} = {result:.2f}\n')
                
    elif option == 6:
        print("\nClosing calculator...")
        is_running = False
    else:
        # When the user enter a different number the calculator prints Invalid Option
        print("\nInvalid Option... Try again.\n")
    
else:
    # This is the last message to the user when he wants to close the calculator
    print('\nCalculator closed\n')
    
print(f'{"=" * 50}')