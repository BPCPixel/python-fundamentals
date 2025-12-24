# This program calculates the area and perimeter of a rectangle
# Area formula: base * height
# Perimeter formula: 2 * (base + height)

print(f'''{"=" * 10} Area and Perimeter of a Rectangle {"=" * 10}
      
AREA = BASE * HEIGHT
PERIMETER = 2 * (BASE + HEIGHT)
''')

# User input
base = float(input('Type the base of the rectangle: '))
height = float(input('Type the height of the rectangle: '))

# Calculations
area = base * height
perimeter = 2 * (base + height)

# Output
print(f'''The area of the rectangle is: {area}
The perimeter of the rectangle is: {perimeter}
      
{"=" * 60}''')
