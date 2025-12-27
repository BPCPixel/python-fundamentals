# This code validates if a person can enter or not to the house of mirrors
# We study If not for this code

print(f'{"=" * 20} House of mirrors {"=" * 20}\n')

# User input
age = int(input('What is your age? '))
afraid_or_not = input('Are you afraid of the dark (Y/N): ').strip().upper()

# If 'Y' Then scared = TRUE
scared = (afraid_or_not == 'Y')

# Validating user data
if not scared and age >= 10:
    print("WELCOME, You can enter the house of mirrors ...")
else:
    print("Sorry, this house could be scary for you ...")

print(f'\n{"=" * 50}')