"""
Simulación de asignación de RAM por el Sistema Operativo.

Autor: Lalo Téllez
"""
import random

print(f'{"=" * 20} Simulación de RAM {"=" * 20}')

# Inicializamos la RAM con espacios vacíos
tamano_ram = int(input('Escribe el tamaño de la RAM: '))
lista_principal = []
for i in range(tamano_ram):
    lista_principal.append("-")

# Listas para guardar la información de los procesos (PCBs)
pcb_pids = []
pcb_nombres = []
pcb_tamanos = []
pcb_estados = []

pid_automatico = 0
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
        nombre_proceso = input('Escribe el nombre del proceso (se recomienda 1 caracter): ')
        
        if nombre_proceso in pcb_nombres:
            print('Error: El nombre del proceso ya existe.')
        else:
            tamano_proceso = int(input('Escribe el tamaño del proceso: '))
            
            # Contar espacios libres en la RAM
            espacio_libre = 0
            for celda in lista_principal:
                if celda == "-":
                    espacio_libre += 1
            
            if tamano_proceso <= espacio_libre:
                # Insertar en los primeros espacios libres que encuentre
                contador = 0
                for i in range(tamano_ram):
                    if lista_principal[i] == "-" and contador < tamano_proceso:
                        lista_principal[i] = nombre_proceso
                        contador += 1
                
                # Guardar datos del PCB
                pid_automatico += 1
                pcb_pids.append(pid_automatico)
                pcb_nombres.append(nombre_proceso)
                pcb_tamanos.append(tamano_proceso)
                
                # Estado aleatorio
                r = random.randint(1, 3)
                if r == 1: estado = "LISTO"
                elif r == 2: estado = "EJECUCIÓN"
                else: estado = "ESPERA"
                pcb_estados.append(estado)
                
                print(f'Proceso {nombre_proceso} creado exitosamente.')
            else:
                print('¡No hay suficiente espacio en la RAM!')

    elif opcion == 2:
        print(f'\n{"-" * 5} Eliminar proceso {"-" * 5}')
        nombre_eliminar = input('Escribe el nombre del proceso a eliminar: ')
        
        if nombre_eliminar in pcb_nombres:
            # 1. Borrar de la RAM (volver a poner '-')
            for i in range(tamano_ram):
                if lista_principal[i] == nombre_eliminar:
                    lista_principal[i] = "-"
            
            # 2. Borrar de las listas de datos (PCB)
            indice = pcb_nombres.index(nombre_eliminar)
            pcb_pids.pop(indice)
            pcb_nombres.pop(indice)
            pcb_tamanos.pop(indice)
            pcb_estados.pop(indice)
            print(f'Proceso {nombre_eliminar} eliminado.')
        else:
            print('Proceso no encontrado.')

    elif opcion == 3:
        print(f'\n{"-" * 5} Buscar proceso {"-" * 5}')
        busqueda = input('Buscar por PID o Nombre: ')
        
        encontrado = False
        for i in range(len(pcb_nombres)):
            # Comparamos con el nombre o con el PID (convertido a texto)
            if busqueda == pcb_nombres[i] or busqueda == str(pcb_pids[i]):
                print(f'Encontrado -> PID: {pcb_pids[i]}, Nombre: {pcb_nombres[i]}, Tamaño: {pcb_tamanos[i]}, Estado: {pcb_estados[i]}')
                encontrado = True
        if not encontrado:
            print('Proceso no encontrado.')

    elif opcion == 4:
        print(f'\n{"-" * 5} Visualizar RAM {"-" * 5}')
        # Mostrar el mapa de la RAM
        print(f'Estado de la RAM: {lista_principal}')
        
        # Mostrar la lista de procesos activos
        print('\nProcesos Activos (PCB):')
        for i in range(len(pcb_nombres)):
            print(f'PID: {pcb_pids[i]} | Nombre: {pcb_nombres[i]} | Tamaño: {pcb_tamanos[i]} | Estado: {pcb_estados[i]}')

    elif opcion == 5:
        print('Saliendo del programa...')
        salir = True
        
print(f'{"=" * 50}')