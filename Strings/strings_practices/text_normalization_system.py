# This program developes a small data normalization for a company 
# The system receives information written by users and It must be processed to generate clean and consistent identifiers

# Name data
name = input('Type your full name: ').strip().title()
normalized_name = name.lower().replace(" ",".")
length_name = len(normalized_name)

# City data
city_code= input('Type your city: ').strip().upper()

# Company data
company = input('Type the name of the company: ').strip()
company_code = company.lower().replace(" ","-")

# Identifiers to generate
username = f'{normalized_name}@{company_code}.com.mx'
internal_ID = f'{city_code}-{length_name}'

# Printing
print(f'''
{'='*10} USER DATA NORMALIZATION {'='*10}

Original name:   {name}
Normalized name: {normalized_name}
Name Length:     {length_name}

City:            {city_code}
Company:         {company_code}

Generated username:
{username}

Internal ID:
{internal_ID}''')