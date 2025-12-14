# Objective: Ask for the name and last name of the user and generate a username
# Format: name.lastname

name = input("What's your name?: ").lower().strip()
last_name = input("What's your last name?: ").lower().strip()

print(f"{name}.{last_name}")

