# Master Formula text[beginning: end : step]
# Slicing allows you to extract a portion of a string.
# Indexing returns a single character, slicing returns a substring.


#  0   1   2   3   4   5   6   7   8   9  10  11
# "P" "R" "O" "G" "R" "A" "M" "A" "C" "I" "O" "N"
# -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
text = "PROGRAMACION"

# 1. Basic [beginning:end]
print(text[0:4]) # PROG (The indice 4 is not included)

# 2. Shortcut from the beginning [:fin]
print(text[:4]) # PROG (Asummes beginning 0)

# 3. Shortcut until the end [beginning:]
print(text[8:]) # CION (Until the last character)

# 4. Negative indices
print(text[-4:]) # CION (The last 4 characters)

# 5. Steps [::step] (inversed string)
print(text[::-1]) # NOICAMARGORP