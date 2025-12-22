# ================================================================
# Employee Salary and Performance Analyzer System
# Practice program to apply string operations, numeric conversion,
# boolean expressions and formatted outputs.
# ================================================================


print(f'{"=" * 10} Employee salary and Performance analyzer system {"=" * 10}')
import random
# Data
name = input(f'Type your full name: ').strip()
company = input(f'Type the name of the company: ').strip()
city = input(f'Type the name of the city you live currently: ').strip()
salary = float(input(f'Type your salary per hour: $').strip())
hours = int(input(f"Number of hours you work during the week: ").strip())

# Normalized data
normalized_name = name.lower().replace(" ",".")
normalized_company = company.lower().replace(" ","-")
normalized_city = city.upper()

# Generate
domain = f'@{normalized_company}-{normalized_city}.com.mx'
email = normalized_name + domain
employee_ID =f'{len(normalized_name)}{normalized_name[:3]}{normalized_company}'
week_salary = hours * salary
code_ID = str(random.randint(0,9999)).zfill(4)

# Boolean comparations
bool_week_salary = (week_salary > 5000)
bool_hours = (hours > 40)
operator_result_and = (bool_week_salary and bool_hours)


print(f'''
*** DATA ***
Name: {name.title()}
Company: {company.title()}
City: {city.title()}
Salary: ${salary}
Worked hours during the week: {hours}

*** Normalized Data ***
Normalized name: {normalized_name}
Normalized company: {normalized_company}
Normalized city: {normalized_city}

*** Generated Data ***
Domain: {domain}
Employee e-mail: {email}
Employee ID: {employee_ID}
Week Salary: ${week_salary}

*** Boolean comparations ***
Bool value of (week salary > 5000) = {bool_week_salary}
Bool value of (hours > 40) = {bool_hours}
Bool value of the logic operator AND of (week salary > 5000 AND hours > 40) = {operator_result_and}
Code ID of the employee: {code_ID}  

{"=" * 60}''')

 