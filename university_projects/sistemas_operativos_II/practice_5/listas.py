"""
Simulación de asignación de RAM por el Sistema Operativo (Listas Ligadas).
Autor: Lalo Téllez (Versión Final)
"""
import random

print(f'{"=" * 20} Simulación de RAM {"=" * 20}')

# 1) Configuración de Hardware definida por el usuario
almacenamiento_kb = int(input('Escribe el tamaño total de la RAM (KB): '))
tamano_bloque_kb = int(input('Escribe el tamaño de cada bloque (KB): '))

# Calculamos el total de bloques (celdas) que tendrá el vector
total_bloques = almacenamiento_kb // tamano_bloque_kb
print(f"Total de bloques disponibles en RAM: {total_bloques}")

# Inicializamos la RAM con el tamaño calculado
lista_principal = ["-" for _ in range(total_bloques)]

# Listas para guardar la información de los procesos (PCB)
pcb_nombres = []
pcb_tamanos_kb = []
pcb_listas_ligadas = [] # Guardará los índices del vector para cada proceso

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
        
        if nombre in pcb_nombres:
            print('Error: El nombre del proceso ya existe.')
        else:
            tam_kb = int(input('Tamaño del proceso (KB): '))
            
            # LÓGICA DE BLOQUES: Si rebasa el múltiplo, se crea uno nuevo
            # Se usa (tam + bloque - 1) // bloque para redondear hacia arriba
            bloques_nec = (tam_kb + tamano_bloque_kb - 1) // tamano_bloque_kb
            
            # Contar espacios libres
            libres = lista_principal.count("-")
            
            if bloques_nec <= libres:
                posiciones = []
                contador = 0
                for i in range(total_bloques):
                    if lista_principal[i] == "-" and contador < bloques_nec:
                        lista_principal[i] = nombre
                        posiciones.append(i)
                        contador += 1
                
                pcb_nombres.append(nombre)
                pcb_tamanos_kb.append(tam_kb)
                pcb_listas_ligadas.append(posiciones)
                print(f'Proceso {nombre} creado. Tamaño {tam_kb}KB -> Ocupa {bloques_nec} bloques.')
            else:
                print(f'Error: No hay espacio. Se requieren {bloques_nec} bloques.')

    elif opcion == 2:
        print(f'\n{"-" * 5} Eliminar proceso {"-" * 5}')
        nombre_del = input('Nombre del proceso a eliminar: ')
        
        if nombre_del in pcb_nombres:
            idx = pcb_nombres.index(nombre_del)
            # Limpiamos la RAM usando su lista ligada
            for pos in pcb_listas_ligadas[idx]:
                lista_principal[pos] = "-"
            
            # Eliminamos de los registros
            pcb_nombres.pop(idx)
            pcb_tamanos_kb.pop(idx)
            pcb_listas_ligadas.pop(idx)
            print(f'Proceso {nombre_del} eliminado.')
        else:
            print('Proceso no encontrado.')

    elif opcion == 3:
        print(f'\n{"-" * 5} Visualizar F.S. (Vectores y Listas) {"-" * 5}')
        # Mostrar el vector físico
        print(f'Vector RAM: {lista_principal}')
        
        # Mostrar la lista ligada de cada proceso (direcciones)
        print('\nListas Ligadas (Direcciones en memoria):')
        for i in range(len(pcb_nombres)):
            # Formato: Proceso A: 0 -> 1 -> 2
            ligado = " -> ".join(map(str, pcb_listas_ligadas[i]))
            print(f'Proceso {pcb_nombres[i]}: {ligado} | Real: {pcb_tamanos_kb[i]} KB')

    elif opcion == 4:
        print('Saliendo...')
        salir = True