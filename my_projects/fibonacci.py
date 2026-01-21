"""
This code iis the fibonacci series
1 1 2 3 5 8 13 21

Author: Lalo Téllez
"""

print(f'{"=" * 20} Fibonacci {"=" * 20}\n')

n = int(input('Type how many values you want to see: '))
a = 0
b = 1
print(a)
print(b)

for i in range(n-2):
    c = a + b
    print(c)
    a = b
    b = c
    
    

print(f'\n{"=" * 50}')
