# This program validates the username and password of the user

# Valid credentials
valid_username = 'admin'
valid_password = '123'

print(f'{"=" * 20} Authentication System {"=" * 20}\n')

# User input
user_input = input('Type your username: ')
password_input = input('Type your password: ')

# Validation
is_authenticated = (user_input == valid_username and password_input == valid_password)

# Output
print(f'''Is your information correct? {is_authenticated}

{"=" * 60}''')
