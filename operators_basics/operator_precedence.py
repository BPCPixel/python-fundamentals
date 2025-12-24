# Operator precedence in Python

print(f'''{"=" * 20} Operator Precedende {"=" * 20}
      
1. Parentheses (): Highest precedence
2. Exponentiation **: Power operator
3. Unary +, -: Positive and negative values
4. Multiplication *, Division /, Floor division //, Modulus %
5. Addition +, Subtraction -
6. Comparisons (==, !=, >, <, >=, <=)
7. Logical operators: not, and, or
8. Assignment operators (=, +=, -=, *=, /=, etc.)

Operator precedence example
1. Floor division: 12 // 3 = 4
2. Multiplication: 2 * 3 = 6
3. Addition: 4 + 6 = 10
4. Subtraction: 10 - 1 = 9

result = 12 // 3 + 2 * 3 - 1
      ''')

# Calculation
result = 12 // 3 + 2 * 3 - 1

# Output
print(f'Result: {result}\n')
print(f'{"=" * 60}')