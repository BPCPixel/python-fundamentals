# This program shows how the replace() function works

# Example
phrase = "Es sal"

print(phrase)
print(phrase.replace("sal", "dulce"))

# Practice: Replace all appearances
message = "Hello World, World"
new_message = message.replace("World", "Python")

# Output: "Hello Python, Python"
print(new_message)

# Replace just once
once = message.replace("World", "Python", 1)

# Output: "Hello Python, World"
print(once)
