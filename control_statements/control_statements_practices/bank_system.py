# This code simulates a system where we study if not

print(f'{"=" * 20} Bank System {"=" * 20}\n')

# User input
ans = input('Do you want to leave the system (Y/N)? ').strip().upper()
leave_system = (ans == 'Y')

# Validating answer
if not leave_system:
    print("We continue in the system ...")
else:
    print("Leaving the system ...")

print(f'\n{"=" * 50}')