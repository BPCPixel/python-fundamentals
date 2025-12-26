# This code checks if a number is positive, negative, or zero

print(f'{"=" * 20} Positive or Not {"=" * 20}\n')

number = int(input("Enter a number: "))

if number > 0:
    print("Your number is positive")
elif number < 0:
    print("Your number is negative")
else:
    print("Your number is zero")

print(f'\n{"=" * 50}')
