import random

print(f'{"=" * 20} SimuFS: Gestión de Archivos {"=" * 20}')

almacenamiento_kb = int(input('Escribe el tamaño total de la RAM (KB): '))
tamano_bloque_kb = int(input('Escribe el tamaño de cada bloque (KB): '))

total_bloques = almacenamiento_kb // tamano_bloque_kb
print(f"Total de bloques disponibles: {total_bloques}")

memoria_ram = ["." for _ in range(total_bloques)]

nombres_procesos = []
tamanos_procesos = []
bloques_asignados = []
propietarios = []

salir = False

while not salir:
    libres = memoria_ram.count(".")
    print(f"\n[ RAM: {libres} bloques libres ]")
    opcion = int(input(f'''
{"-" * 5} MENÚ DE USUARIO {"-" * 5}
1. Crear archivo
2. Eliminar archivo
3. Visualizar
4. Buscar
5. Modificar
6. Salir
OPCIÓN: '''))

    if opcion == 1:
        nombre = input('Nombre del archivo (1 carácter): ')
        if len(nombre) != 1:
            print('Error: El nombre debe ser de un solo carácter.')
        elif nombre in nombres_procesos:
            print('Error: El nombre ya existe.')
        else:
            propietario = input('Nombre del propietario: ')
            tam_kb = int(input('Tamaño del archivo (KB): '))

            bloques_nec = (tam_kb + tamano_bloque_kb - 1) // tamano_bloque_kb

            if bloques_nec <= memoria_ram.count("."):
                posiciones = []
                contador = 0
                for i in range(total_bloques):
                    if memoria_ram[i] == "." and contador < bloques_nec:
                        memoria_ram[i] = nombre
                        posiciones.append(i)
                        contador += 1

                nombres_procesos.append(nombre)
                tamanos_procesos.append(tam_kb)
                bloques_asignados.append(posiciones)
                propietarios.append(propietario)
                print(f'Archivo [{nombre}] creado por {propietario}.')
            else:
                print('Error: Espacio insuficiente.')

    elif opcion == 2:
        nombre_del = input('Nombre del archivo a eliminar: ')
        if nombre_del in nombres_procesos:
            idx = nombres_procesos.index(nombre_del)
            dueno_val = input(f'Ingrese el nombre del propietario de {nombre_del}: ')

            if propietarios[idx] == dueno_val: # Validación de dueño
                for pos in bloques_asignados[idx]:
                    memoria_ram[pos] = "."
                nombres_procesos.pop(idx)
                tamanos_procesos.pop(idx)
                bloques_asignados.pop(idx)
                propietarios.pop(idx)
                print('Eliminado exitosamente.')
            else:
                print('Error: Propietario incorrecto.')
        else:
            print('No encontrado.')

    elif opcion == 3:
        print(f'\nVector de almacenamiento: {"".join([f"[{b}]" for b in memoria_ram])}')
        for i in range(len(nombres_procesos)):
            ruta = " -> ".join([f"[{b + 1}]" for b in bloques_asignados[i]])
            print(f'Archivo: {nombres_procesos[i]} | Dueño: {propietarios[i]} | Ruta: {ruta}')

    elif opcion == 4:
        nombre_busq = input('Nombre del archivo a buscar: ')
        if nombre_busq in nombres_procesos:
            idx = nombres_procesos.index(nombre_busq)
            print(f"Archivo: {nombres_procesos[idx]} | Tamaño: {tamanos_procesos[idx]}KB | Dueño: {propietarios[idx]}")
        else:
            print("Archivo no encontrado.")

    elif opcion == 5:
        nombre_mod = input('Nombre del archivo a modificar: ')
        if nombre_mod in nombres_procesos:
            idx = nombres_procesos.index(nombre_mod)
            dueno_val = input(f'Ingrese el nombre del propietario de {nombre_mod}: ')

            if propietarios[idx] == dueno_val:
                print(f'Tamaño actual: {tamanos_procesos[idx]} KB')
                cambio_kb = int(input('KB a sumar (+) o restar (-): '))
                nuevo_tam = tamanos_procesos[idx] + cambio_kb

                if nuevo_tam < 0:
                    print('Error: El tamaño no puede ser menor a 0.')
                else:

                    bloques_n = (nuevo_tam + tamano_bloque_kb - 1) // tamano_bloque_kb
                    bloques_a = len(bloques_asignados[idx])
                    dif = bloques_n - bloques_a

                    if dif > 0:
                        if dif <= memoria_ram.count("."):
                            c = 0
                            for i in range(total_bloques):
                                if memoria_ram[i] == "." and c < dif:
                                    memoria_ram[i] = nombre_mod
                                    bloques_asignados[idx].append(i)
                                    c += 1
                            tamanos_procesos[idx] = nuevo_tam
                            print('Tamaño aumentado.')
                        else:
                            print('Error: No hay espacio para aumentar.')
                    elif dif < 0:
                        for _ in range(abs(dif)):
                            pos = bloques_asignados[idx].pop()
                            memoria_ram[pos] = "."
                        tamanos_procesos[idx] = nuevo_tam
                        print('Tamaño reducido.')
                    else:
                        tamanos_procesos[idx] = nuevo_tam
                        print('Tamaño actualizado (mismos bloques).')
            else:
                print('Error: Propietario incorrecto.')

    elif opcion == 6:
        print("Saliendo del simulador...")
        salir = True