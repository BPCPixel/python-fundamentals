# The elif statement is an abbreviation of "else if" and is used
# to evaluate multiple conditions

print(f'{"=" * 20} elif Statement {"=" * 20}\n')

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
elif 13 <= age < 18:
    print("You are a teenager")
else:
    print("You are a kid")

print(f'\n{"=" * 50}')
