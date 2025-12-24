# This program practices the logical operator OR
# A library loans books if at least one condition is met:
# 1. The user has a student credential
# 2. The user lives no more than 3 km away

print(f'''{"=" * 20} Book Loan System {"=" * 20}

Allowed distance: 3KM''')

# Valid distance
allowed_distance = 3

# User input
credential = input("Do you have a student credential? (Y/N): ").strip().upper()
distance_km = int(input("How many kilometers away do you live?: "))

# Logical validation
loan_book = (credential == "Y" or distance_km <= allowed_distance)

# Result
print(f'''
Can a book be loaned to you? = {loan_book}

{"=" * 60}''')


