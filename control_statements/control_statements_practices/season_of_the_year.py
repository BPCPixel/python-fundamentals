# This code ask the user to identify the season of the year
print(f'{"=" * 10} Identify the season of the year {"=" * 10}\n')

# Informative Menu
print(f'''{"-" * 10} MONTHS {"-" * 10}
1 - JANUARY
2 - FEBRUARY
3 - MARCH
4 - APRIL
5 - MAY
6 - JUNE
7 - JULY
8 - AUGUST
9 - SEPTEMBER
10 - OCTOBER
11 - NOVEMBER
12 - DECEMBER\n''')

# User input
month = int(input("Insert the number of a month (1-12): "))

# Validation
season = None # It has a FALSE value

# Identifying the season with IF-ELIF
if month in (12, 1, 2):
    season = 'Winter'
elif 3 <= month <= 5:
    season = 'Spring'
elif 6 <= month <= 8:
    season = 'Summer'
elif 9 <= month <= 11:
    season = 'Fall'
    
# If season has a value (not None or empty), it evaluates to True
if season:
    print(f'The month number {month} belongs to {season}')
else:
    print(f'Invalid month number. Please enter a value between 1 and 12')
    
print(f'\n{"=" * 50}') 
