"""
Practice: ATM Program

This program simulates an ATM system to practice while loops.

Author: Lalo Tellez
"""

print(f'{"=" * 20} ATM Practice Program {"=" * 20}\n')

# Initial balance
balance = 0.0

# Control variable for the main loop
is_running = True

while is_running:
    print(f'''Available operations:
    1. Check balance
    2. Withdraw
    3. Deposit
    4. Exit''')

    option = int(input('Select an option: '))

    if option == 1:
        print(f'Balance: ${balance:.2f}\n')

    elif option == 2:

        # If the user has insufficient funds it won't perform
        if balance == 0:
            print("Insufficient funds to perform a withdrawal.\n")
        else:
            withdraw = float(input('Enter the amount you would like to withdraw: $'))
            
            # Validation
            if withdraw > balance:
                print("The amount you want to withdraw is greater than your current balance.\n")
            else:
                balance -= withdraw
                print('\nTransaction successful.')

    elif option == 3:
        deposit = float(input('Enter the amount you would like to deposit: $'))
        balance += deposit
        print('\nTransaction successful.')

    elif option == 4:
        print('Exiting the system...\n')
        is_running = False

    else:
        print('Invalid option. Please try again.\n')
else:
    print('ATM system closed.')

print(f'\n{"=" * 50}')
