# Objective: ask for the full name of the user and print processed information.

full_name = input("What is your full name? ").strip()
upper_full_name = full_name.upper()
length = len(upper_full_name)

print(f"""
Processed name: {upper_full_name}
Length: {length}
First letter: {upper_full_name[0]}
Last letter: {upper_full_name[-1]}
First 3 letters: {upper_full_name[0:3]}
Last 3 letters: {upper_full_name[-3:]}
""")
