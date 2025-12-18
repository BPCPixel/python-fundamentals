# Program shows how function bool works

print('=' * 20 + " Function Bool " + '=' * 20)

# 1. Numbers (int and float)
print(f"0 = {bool(0)}") # False: empty number
print(f"0.0 = {bool(0.0)}") # False
print(f"42 = {bool(42)}") # True: exist value

# 2. Text (strings)
# Empty string = nothing = Flse
print(f"''= {bool("")}") # False

# String with space or text= something = True
print(f"' ' = {bool(" ")}")
print(f'Hola = {bool("Hola")}')

# 3. None
empty = None
print(f'empty: {bool(empty)}')
print(f'False = {bool(False)}')
print(f'True = {bool(True)}')

print("=" * 55)