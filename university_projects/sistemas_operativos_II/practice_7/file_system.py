"""
Simulador de Sistema de Archivos Navegable
Autor: Lalo Téllez
"""
import random

print(f'{"=" * 20} Sistema de Archivos {"=" * 20}')

nombres_elementos = ["C:"]  
tipos_elementos = ["Carpeta"]
padres_elementos = [None]   
tamanos_archivos = [0]      

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
            padres_elementos.append(ubicacion_actual)
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
            padres_elementos.append(ubicacion_actual)
            tamanos_archivos.append(tam_kb)
            print(f'Archivo [{nombre}] creado en {ubicacion_actual}.')

    elif opcion == 3:
        destino = input('Ingrese nombre de una carpeta existente para entrar: ')
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
            print("Ya estas en el tronco principal.")
        else:
            idx_actual = nombres_elementos.index(ubicacion_actual)
            ubicacion_actual = padres_elementos[idx_actual]
            print(f'Saliste a {ubicacion_actual}')

    elif opcion == 5:
        print(f'\n{"=" * 15} EXPLORADOR DE ARCHIVOS {"=" * 15}')
        print(f"{'NOMBRE':<25} | {'TIPO':<10} | {'TAMAÑO':<10}")
        print("-" * 52)
        
        # Tronco principal
        print(f"📁 [{nombres_elementos[0]}]")
        
        for i in range(len(nombres_elementos)):
           
            if padres_elementos[i] == nombres_elementos[0]:
                if tipos_elementos[i] == "Carpeta":
                    
                    peso_carpeta = 0
                    for k in range(len(nombres_elementos)):
                        if padres_elementos[k] == nombres_elementos[i]:
                            peso_carpeta += tamanos_archivos[k]
                    
                    print(f" ├── 📁 {nombres_elementos[i]:<18} | {'Carpeta':<10} | {peso_carpeta:>7} KB")
                    
                    for j in range(len(nombres_elementos)):
                        if padres_elementos[j] == nombres_elementos[i]:
                            if tipos_elementos[j] == "Archivo":
                                print(f" │    └── 📄 {nombres_elementos[j]:<13} | {'Archivo':<10} | {tamanos_archivos[j]:>7} KB")
                            else:
                                print(f" │    └── 📁 {nombres_elementos[j]:<13} | {'Carpeta':<10} | {'-':>7}")
                else:
                    print(f" ├── 📄 {nombres_elementos[i]:<18} | {'Archivo':<10} | {tamanos_archivos[i]:>7} KB")
        
        print("-" * 52)

    elif opcion == 6:
        print("Saliendo...")
        salir = True