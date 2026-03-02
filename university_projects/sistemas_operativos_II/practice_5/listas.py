"""
Simulación de asignación de RAM por el Sistema Operativo (Listas Ligadas).
Autor: Lalo Téllez (Versión Final - Posiciones Humanas)
"""

print(f'{"=" * 20} Simulación de RAM {"=" * 20}')

# 1) Configuración de Hardware
almacenamiento_kb = int(input('Escribe el tamaño total de la RAM (KB): '))
tamano_bloque_kb = int(input('Escribe el tamaño de cada bloque (KB): '))

total_bloques = almacenamiento_kb // tamano_bloque_kb
print(f"Total de bloques disponibles en RAM: {total_bloques}")

memoria_ram = ["." for _ in range(total_bloques)]

nombres_procesos = []
tamanos_procesos = []
bloques_asignados = [] 

salir = False

while not salir:
    opcion = int(input(f'''
{"-" * 5} MENÚ DE USUARIO {"-" * 5}
1. Crear proceso
2. Eliminar proceso
3. Visualizar RAM y Listas Ligadas
4. Salir
OPCIÓN: '''))

    if opcion == 1:
        print(f'\n{"-" * 5} Creando proceso {"-" * 5}')
        nombre = input('Nombre del proceso: ')
        
        if nombre in nombres_procesos:
            print('Error: El nombre del proceso ya existe.')
        else:
            tam_kb = int(input('Tamaño del proceso (KB): '))
            bloques_nec = (tam_kb + tamano_bloque_kb - 1) // tamano_bloque_kb
            libres_antes = memoria_ram.count(".")
            
            if bloques_nec <= libres_antes:
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
                
                libres_ahora = memoria_ram.count(".")
                print(f'Proceso [{nombre}] creado. Ocupó {bloques_nec} bloques. (Disponibles: {libres_ahora})')
            else:
                print(f'Error: No hay espacio. Se requieren {bloques_nec} bloques.')

    elif opcion == 2:
        print(f'\n{"-" * 5} Eliminar proceso {"-" * 5}')
        nombre_del = input('Nombre del proceso a eliminar: ')
        
        if nombre_del in nombres_procesos:
            idx = nombres_procesos.index(nombre_del)
            for pos in bloques_asignados[idx]:
                memoria_ram[pos] = "."
            
            nombres_procesos.pop(idx)
            tamanos_procesos.pop(idx)
            bloques_asignados.pop(idx)
            print(f'Proceso [{nombre_del}] eliminado.')
        else:
            print('Proceso no encontrado.')

    elif opcion == 3:
        print(f'\n{"-" * 5} ESTADO DE LA MEMORIA {"-" * 5}')
        
        print("\nVector RAM:")
        visual_vector = "".join([f"[{bloque}]" for bloque in memoria_ram])
        print(visual_vector)
        
        print('\nListas Ligadas (Ruta):')
        for i in range(len(nombres_procesos)):
            # Sumamos +1 a cada bloque para que empiece desde 1 en la visualización
            ruta = " - ".join([f"[{b + 1}]" for b in bloques_asignados[i]])
            print(f'{nombres_procesos[i]} -> {ruta}')
        print("-" * 30)

    elif opcion == 4:
        print('Saliendo del sistema...')
        salir = True