# Objective: Create a program to generate an email from user data
# Name: [full_name]
# Company: [company_name]
# Domain: [domain_name]
# Final result: email: name.last_name@company_name.com.mx

full_name = input("Type your full name: ")
normalized_full_name = full_name.strip().lower().replace(" ", ".")

company_name = input("Type the company name: ")
domain = ".com.mx"
normalized_company = company_name.strip().lower().replace(" ", ".")
normalized_email_domain = f"@{normalized_company}{domain}"

print(f"""
{'*' * 10} Email Generator {'*' * 10}

User name: {full_name.strip().title()}
Normalized user name: {normalized_full_name}

Company name: {company_name.strip().title()}
Domain extension: {domain}
Normalized email domain: {normalized_email_domain}

Final generated email:
{normalized_full_name}{normalized_email_domain}
""")
