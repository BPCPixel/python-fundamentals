# Example: string immutability

animal = "Cat"

# animal[3] = "S"  # This causes an error because strings are immutable

# Correct approach: create a new string using concatenation
plural = animal + "s"

print(animal)   # Output: Cat (unchanged)
print(plural)   # Output: Cats (new object)

# Using f-strings
plural = f"{animal}s"
print(plural)   # Output: Cats (new object)
