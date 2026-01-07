"""
This is an Udemy Test where I need to print just the number of vowels in a string.

Author: Lalo Téllez
"""

# Declarar la variable
cadena = 'Hola Mundo'.lower()
# Agregar el ciclo for
contador = 0
for i in cadena:
    if i == 'a':
        contador += 1
    elif i == 'e':
        contador += 1
    elif i == 'i':
        contador += 1
    elif i == 'o':
        contador += 1
    elif i == 'u':
        contador += 1
# Imprimir la cantidad de vocales encontradas en la cadena
print(contador)