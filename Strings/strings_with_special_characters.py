# When we use "\" it means the next character is treated as a special character
# This is called a BACKSLASH or escape character

message = "She said \"Hi\" as she got in"
print(message)

# New line character "\n"
# This character moves the text to the next line, like pressing 'Enter'
print("Hello\nWorld\nI'm Lalo")

# Tab character "\t"
# Inserts a horizontal tab (spacing depends on the environment)
print("Name:\tJuan")
print("Last name:\tPérez")

# \" Double quotes
# Allows printing double quotes inside a string delimited by double quotes
print("The book's name is: \"1984\"")

# \' Single quotes
# Essential when a string is delimited by single quotes and contains an apostrophe
print('Jose O\'Gorman')

# Raw string r
# When we want to use the character "\" we need to use double \\ backslash or using r + double quotes r"message"
path = r"C:\Users\lalot\Documents"
print(path)