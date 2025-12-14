# This program shows string concatenation in Python

name = "Ana"
age = 20

print(f"Your name is {name}, your age is {age}")

# 1. Using the + operator
name = "Lucia"
last_name = "Garcia"
full_name = name + " " + last_name

# 2. Using print() with commas
age = 21
print("Using commas:", "Name:", full_name, ", Age:", age)

# 3. Using f-strings (recommended)
city = "Barcelona"
country = "Spain"
profession = "Engineer"

presentation = (
    f"Hi! I'm {full_name}, I'm {age + 1} years old "
    f"and I'm an {profession} in {city}, {country}"
)

print(presentation)
