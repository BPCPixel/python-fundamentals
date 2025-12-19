# Objective: Ask for a word, clean it and transform it into uppercase

word = input("Type a word: ").upper().strip()
length = len(word)
half = length // 2

print(f"""
Word: {word}
Length: {length}
First half: {word[0:half]}
Second half: {word[half:]}
""")
