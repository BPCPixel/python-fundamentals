"""
Simulación de asignación de RAM por el Sistema Operativo utilizando marcos, bloques y páginas.

Autor: Lalo Téllez
"""
import random

print(f'{"=" * 20} Simulación de RAM {"=" * 20}')

salir = False
while salir != True:
    opcion = int(input(f'''
{"-" * 5} MENÚ DE USUARIO {"-" * 5}
1. Crear procesos
2. Eliminar procesos
3. Buscar procesos
4. Visualizar procesos en RAM
5. Salir
OPCIÓN: '''))

    if opcion == 1:
        print(f'\n{"-" * 5} Creando proceso {"-" * 5}')
        

    elif opcion == 2:
        print(f'\n{"-" * 5} Eliminar proceso {"-" * 5}')
        

    elif opcion == 3:
        print(f'\n{"-" * 5} Buscar proceso {"-" * 5}')
        

    elif opcion == 4:
        print(f'\n{"-" * 5} Visualizar RAM {"-" * 5}')
        

    elif opcion == 5:
        print('Saliendo del programa...')
        salir = True
        
print(f'{"=" * 50}')