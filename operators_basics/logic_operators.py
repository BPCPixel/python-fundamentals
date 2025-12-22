# Logical operators are used to perform logical operations with boolean values.
# The AND operator returns True if both expressions are True; otherwise, it returns False.
# The OR operator returns True if at least one of the conditions is True; otherwise, it returns False.
# The NOT operator inverts the boolean value, True turns False and False turns True

x, y = 1, 10;
print(f''' {"=" * 20} Logic Operators {"=" * 20}

{"*"*10} TRUTH TABLES {"*"*10}
X = {x}, Y = {y}
AND value
| X || Y || X AND Y ||
|---||---||---------||
| T || T ||    T    ||
| T || F ||    F    ||
| F || T ||    F    ||
| F || F ||    F    ||
x > 5 AND y > 5 = {x > 5 and y > 5}

X = {x}, Y = {y}
OR value
| X || Y || X  OR  Y ||
|---||---||----------||
| T || T ||     T    ||
| T || F ||     T    ||
| F || T ||     T    ||
| F || F ||     F    ||
x > 5 OR y > 5 = {x > 5 or y > 5}

X = {x}, Y = {y}
NOT value
| X || Y || NOT X || NOT Y ||
|---||---||-------||-------||
| T || T ||   F   ||   F   ||
| T || F ||   F   ||   T   ||
| F || T ||   T   ||   F   ||
| F || F ||   T   ||   T   ||
NOT (X > Y) = {not x > y} NOT (Y > X) = {not y > x}

{"=" * 60}''')
