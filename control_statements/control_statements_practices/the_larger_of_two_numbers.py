# This code checks what number is larger
print(f'{"=" * 20} The larger of two numbers {"=" * 20}\n')

# User input
first_number = int(input("Type a number: "))
second_number = int(input("Type another number: "))

# Validation of the two numbers and output
if first_number > second_number:
    print(f'The number {first_number} is larger than {second_number}')
elif first_number < second_number:
    print(f'The number {second_number} is larger than {first_number}')
else:
    print(f'The number {first_number} and the number {second_number} are the same.')

print(f'\n{"=" * 50}')