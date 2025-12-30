"""
Authentication System V2

This code is a new version of the Authentication System
where it validates the username and the password of the user
and it prints if the credentials are correct or not

Author: Lalo Tellez
"""

print(f'{"=" * 20} Authentication System V2 {"=" * 20}\n')

# We define user and password as CONSTANTS
USERNAME = "admin"
PASSWORD = "123"

# Welcome message to user
print('''Hello, there!
      
Enter your correct username and password to access the system''')

# User input
username = input('Username: ')
password = input('Password: ') 

# Validation flags
valid_user = (username == USERNAME)
valid_password = (password == PASSWORD)

# Authentication Logic
if valid_user and valid_password:
    message = 'Welcome to the system!'
elif valid_user and not valid_password:
    message = 'Incorrect password, try again.'
elif not valid_user and valid_password:
    message = 'Incorrect username, try again.'
else:
    message = 'Incorrect username and password, try again.'

# Output
print(f'\n{message}')
print(f'\n{"=" * 50}')