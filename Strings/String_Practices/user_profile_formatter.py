# Objective: Create a program that recives a raw user data and generates a clean and formatted profile summary,
# similar to what a real system would display after normalizing user input


# Requirements
full_name = input("Type your full name: ") # may include extra spaces
city = input("Type your city: ").title()
f_programmingLanguage = input ("Type your favorite programming language: ").upper().strip()

normalized_full_name = full_name.strip().upper()
username = full_name.strip().lower().replace(" ",".")
initials = normalized_full_name[0] + normalized_full_name[normalized_full_name.find(" ") + 1]
total_letters = len(full_name.replace(" ",""))
first_three = normalized_full_name[:3]
last_three = normalized_full_name[-3:]

# Printing
print("=" * 10, "USER PROFILE FORMATTER", "=" * 10)
print(f"""
Normalized Name: {normalized_full_name}
Username: {username}
Initials: {initials}

City: {city}
Language: {f_programmingLanguage}

Total letters (no spaces): {total_letters}
First 3 Letters: {first_three}
Last 3 Letters: {last_three}

{'='*35}
      """)