# This program asks the user for a value and checks if it is in or out of range

print(f'{"=" * 20} In - Out Range Program {"=" * 20}\n')

# Define constant values
min_value = 0
max_value = 5

# User input
value = int(input('Type a value between 0 and 5: '))

# Validation
is_in_range = (min_value <= value <= max_value)

# Output
print(f'''Is the value IN range?  = {is_in_range}
Is the value OUT of range? = {not is_in_range}

{"=" * 60}''')
