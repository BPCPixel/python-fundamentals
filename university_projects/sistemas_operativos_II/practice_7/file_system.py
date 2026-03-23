"""
Simulador de Sistema de Archivos Navegable (Árbol)
Autor: Lalo Téllez
"""
import random

print(f'{"=" * 20} Sistema de Archivos: Terminal Simple {"=" * 20}')

# Estructuras para la jerarquía
nombres_elementos = ["C:"]  
tipos_elementos = ["Carpeta"]
padres_elementos = [None]   
tamanos_archivos = [0]      

# Variable de navegación (Ubicación actual)
ubicacion_actual = "C:"

salir = False
while not salir:
    print(f"\nRuta actual: {ubicacion_actual}/")
    opcion = int(input(f'''
{"-" * 5} MENÚ TERMINAL {"-" * 5}
1. Crear Carpeta
2. Crear Archivo 
3. Entrar a Carpeta
4. Salir a Carpeta Padre
5. Visualizar Árbol Completo
6. Salir
OPCIÓN: '''))

    if opcion == 1:
        nombre = input('Nombre de la nueva carpeta: ')
        if nombre in nombres_elementos:
            print('Error: El nombre ya existe en el sistema.')
        else:
            nombres_elementos.append(nombre)
            tipos_elementos.append("Carpeta")
            padres_elementos.append(ubicacion_actual) # Se crea dentro de donde estoy
            tamanos_archivos.append(0)
            print(f'Carpeta [{nombre}] creada en {ubicacion_actual}.')

    elif opcion == 2:
        nombre = input('Nombre del archivo: ')
        if nombre in nombres_elementos:
            print('Error: El nombre ya existe.')
        else:
            tam_kb = int(input('Tamaño (KB): '))
            nombres_elementos.append(nombre)
            tipos_elementos.append("Archivo")
            padres_elementos.append(ubicacion_actual) # Se crea dentro de donde estoy
            tamanos_archivos.append(tam_kb)
            print(f'Archivo [{nombre}] creado en {ubicacion_actual}.')

    elif opcion == 3:
        destino = input('Ingrese nombre de una carpeta existente para entrar: ')
        # Validar que exista, que sea carpeta y que sea hija de la actual
        existe = False
        for i in range(len(nombres_elementos)):
            if nombres_elementos[i] == destino and tipos_elementos[i] == "Carpeta" and padres_elementos[i] == ubicacion_actual:
                ubicacion_actual = destino
                print(f'Entraste a {ubicacion_actual}')
                existe = True
                break
        if not existe:
            print("Error: La carpeta no existe en esta ubicación.")

    elif opcion == 4:
        if ubicacion_actual == "C:":
            print("Ya estás en el tronco principal.")
        else:
            # Buscar quién es el padre de la ubicación actual
            idx_actual = nombres_elementos.index(ubicacion_actual)
            ubicacion_actual = padres_elementos[idx_actual]
            print(f'Saliste a {ubicacion_actual}')

    elif opcion == 5:
        print(f'\n{"=" * 10} ESTRUCTURA DEL ÁRBOL {"=" * 10}')
        # Visualización simple por niveles
        print(f"[{nombres_elementos[0]}]")
        for i in range(len(nombres_elementos)):
            if padres_elementos[i] == nombres_elementos[0]:
                print(f" ├── 📁 {nombres_elementos[i]}")
                # Buscar nietos
                for j in range(len(nombres_elementos)):
                    if padres_elementos[j] == nombres_elementos[i]:
                        prefix = " 📄 " if tipos_elementos[j] == "Archivo" else " 📁 "
                        print(f" │    └──{prefix}{nombres_elementos[j]}")

    elif opcion == 6:
        salir = True