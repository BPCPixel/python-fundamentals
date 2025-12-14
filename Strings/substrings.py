# This program demonstrates how to use substrings

phrase = "Hello, World!"

# Finding the index of a substring
index = phrase.find("World")

print(f"""
Phrase: {phrase}
Index "World": {index}
""")

index = phrase.find("Hello")
print(f"""
Phrase: {phrase}
Index "Hello": {index}
""")
