# Check if a variable is in range between 1 and 10

data = int(input('Type an integer number: '))

# Check if the value is in range
in_range = 1 <= data <= 10
print(f'Is the variable in range (1 to 10)? {in_range}')

# Using NOT operator
out_range = not in_range
print(f'Is the variable out of range? {out_range}')
