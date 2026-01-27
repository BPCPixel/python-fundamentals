"""
Simulación de RAM con MATRICES.
Autor: Lalo Téllez 
"""
import random

print(f'{"=" * 20} Simulación de RAM Contigua {"=" * 20}')

filas = int(input('Escribe el número de filas: '))
columnas = int(input('Escribe el número de columnas: '))

matriz_ram = []
for f in range(filas):
    fila_nueva = []
    for c in range(columnas):
        fila_nueva.append("-")
    matriz_ram.append(fila_nueva)

pcb_pids = []
pcb_nombres = []
pcb_tamanos = []
pcb_estados = []

pid_automatico = 0
salir = False

while salir != True:
    opcion = int(input(f'''
{"-" * 5} MENÚ {"-" * 5}
1. Crear proceso
2. Eliminar proceso
3. Buscar proceso
4. Visualizar RAM
5. Salir
OPCIÓN: '''))

    if opcion == 1:
        nombre_proceso = input('Nombre del proceso: ')
        if nombre_proceso in pcb_nombres:
            print('Error: El nombre ya existe.')
        else:
            tamano_proceso = int(input('Tamaño del proceso: '))
            
            # Se busca un bloque
            inicio_encontrado = -1
            capacidad_total = filas * columnas
            
            # Recorremos la RAM como si fuera una sola línea larga
            for i in range(capacidad_total - tamano_proceso + 1):
                es_posible = True
                for j in range(tamano_proceso):
                    
                    f_temp = (i + j) // columnas
                    c_temp = (i + j) % columnas
                    
                    if matriz_ram[f_temp][c_temp] != "-":
                        es_posible = False
                        break
                
                if es_posible:
                    inicio_encontrado = i
                    break
            
            if inicio_encontrado != -1:
                # Insertar el proceso en el bloque
                for k in range(tamano_proceso):
                    f_pos = (inicio_encontrado + k) // columnas
                    c_pos = (inicio_encontrado + k) % columnas
                    matriz_ram[f_pos][c_pos] = nombre_proceso
                
                pid_automatico += 1
                pcb_pids.append(pid_automatico)
                pcb_nombres.append(nombre_proceso)
                pcb_tamanos.append(tamano_proceso)
                
                estados_posibles = ["LISTO", "EJECUCIÓN", "ESPERA"]
                pcb_estados.append(random.choice(estados_posibles))
                print(f'Proceso {nombre_proceso} asignado')
            else:
                print('Error: No se encontró un bloque suficiente.')

    elif opcion == 2:
        nombre_eliminar = input('Proceso a eliminar: ')
        if nombre_eliminar in pcb_nombres:
            for f in range(filas):
                for c in range(columnas):
                    if matriz_ram[f][c] == nombre_eliminar:
                        matriz_ram[f][c] = "-"
            indice = pcb_nombres.index(nombre_eliminar)
            pcb_pids.pop(indice); pcb_nombres.pop(indice)
            pcb_tamanos.pop(indice); pcb_estados.pop(indice)
            print('Proceso eliminado.')
        else:
            print('No encontrado.')

    elif opcion == 3:
        busqueda = input('PID o Nombre: ')
        encontrado = False
        for i in range(len(pcb_nombres)):
            if busqueda == pcb_nombres[i] or busqueda == str(pcb_pids[i]):
                print(f'PID: {pcb_pids[i]}, Nombre: {pcb_nombres[i]}, Tam: {pcb_tamanos[i]}, Estado: {pcb_estados[i]}')
                encontrado = True
        if not encontrado: print('No encontrado.')

    elif opcion == 4:
        print(f'\nMapa de Memoria ({filas}x{columnas}):')
        for f in range(filas):
            print(f"{matriz_ram[f]}")

    elif opcion == 5:
        salir = True

print(f'{"=" * 50}')