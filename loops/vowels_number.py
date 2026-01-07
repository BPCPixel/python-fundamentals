"""
Udemy Test: Count Vowels in a String

This program counts and prints the number of vowels in a string.

Author: Lalo Tellez
"""

# Declare the string and convert it to lowercase
text = 'Hola Mundo'.lower()

vowels = 'aeiou'

# Initialize the vowel counter
vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1

# Print the number of vowels found in the string
print(vowel_count)
