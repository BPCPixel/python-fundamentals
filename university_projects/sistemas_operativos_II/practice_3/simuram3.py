import random

print(f'{"=" * 20} Simulación de RAM por Marcos {"=" * 20}')

# Configuración inicial
tamano_ram_kb = 100
tamano_marco_kb = 4
total_bloques = tamano_ram_kb // tamano_marco_kb # 25 bloques

# Inicializamos la RAM (el vector de 25 espacios)
lista_principal = []
for i in range(total_bloques):
    lista_principal.append("-")

# Listas para el PCB (Control de procesos)
pcb_pids = []
pcb_nombres = []
pcb_tamanos_kb = []
pcb_marcos_usados = [] # Guardaremos una lista de índices para cada proceso

pid_automatico = 0
salir = False

while not salir:
    opcion = int(input(f'''
{"-" * 10} MENÚ DE GESTIÓN DE MEMORIA {"-" * 10}
RAM Total: {tamano_ram_kb}KB | Marcos: {total_bloques} de {tamano_marco_kb}KB
1. Crear proceso
2. Eliminar proceso (PID o Nombre)
3. Buscar proceso (PID, Nombre, Marco o Página)
4. Visualizar RAM y PCB
5. Salir
OPCIÓN: '''))

    if opcion == 1:
        print(f'\n{"-" * 5} Creando proceso {"-" * 5}')
        nombre = input('Nombre del proceso: ')
        
        if nombre in pcb_nombres:
            print('Error: El nombre ya existe.')
        else:
            tamano_solicitado = int(input('Tamaño del proceso en KB: '))
            # Calcular cuántos marcos necesita (Redondeo hacia arriba)
            # Ejemplo: 6KB / 4KB = 1.5 -> Necesita 2 marcos
            marcos_necesarios = (tamano_solicitado + tamano_marco_kb - 1) // tamano_marco_kb
            
            # --- LÓGICA DE BÚSQUEDA BEST-FIT (El mejor ajuste) ---
            mejor_inicio = -1
            mejor_tamano_hueco = total_bloques + 1
            
            i = 0
            while i < total_bloques:
                if lista_principal[i] == "-":
                    inicio_hueco = i
                    tamano_hueco = 0
                    while i < total_bloques and lista_principal[i] == "-":
                        tamano_hueco += 1
                        i += 1
                    
                    # ¿Cabe el proceso y es el hueco más pequeño que hemos visto?
                    if tamano_hueco >= marcos_necesarios and tamano_hueco < mejor_tamano_hueco:
                        mejor_tamano_hueco = tamano_hueco
                        mejor_inicio = inicio_hueco
                else:
                    i += 1

            if mejor_inicio != -1:
                indices_asignados = []
                for k in range(marcos_necesarios):
                    posicion = mejor_inicio + k
                    lista_principal[posicion] = nombre
                    indices_asignados.append(posicion)
                
                # Guardar en PCB
                pid_automatico += 1
                pcb_pids.append(pid_automatico)
                pcb_nombres.append(nombre)
                pcb_tamanos_kb.append(tamano_solicitado)
                pcb_marcos_usados.append(indices_asignados)
                
                print(f'Proceso "{nombre}" creado. Usó {marcos_necesarios} marcos.')
            else:
                print('Error: No hay un bloque contiguo suficiente para el proceso.')

    elif opcion == 2:
        print(f'\n{"-" * 5} Eliminar proceso {"-" * 5}')
        dato = input('Escribe el PID o Nombre a eliminar: ')
        indice_pcb = -1
        
        # Buscar el índice en el PCB
        for i in range(len(pcb_nombres)):
            if dato == pcb_nombres[i] or dato == str(pcb_pids[i]):
                indice_pcb = i
                break
        
        if indice_pcb != -1:
            nombre_borrar = pcb_nombres[indice_pcb]
            # Limpiar RAM
            for i in range(total_bloques):
                if lista_principal[i] == nombre_borrar:
                    lista_principal[i] = "-"
            
            # Eliminar de listas
            pcb_pids.pop(indice_pcb)
            pcb_nombres.pop(indice_pcb)
            pcb_tamanos_kb.pop(indice_pcb)
            pcb_marcos_usados.pop(indice_pcb)
            print(f'Proceso {nombre_borrar} eliminado.')
        else:
            print('Proceso no encontrado.')

    elif opcion == 3:
        print(f'\n{"-" * 5} Buscar proceso {"-" * 5}')
        busqueda = input('Buscar por PID, Nombre, Marco o Página: ')
        encontrado = False
        
        for i in range(len(pcb_nombres)):
            # Verificar PID o Nombre
            es_proceso = (busqueda == pcb_nombres[i] or busqueda == str(pcb_pids[i]))
            
            # Verificar si la búsqueda es un Marco o Página (índice)
            es_marco_pag = False
            if busqueda.isdigit():
                if int(busqueda) in pcb_marcos_usados[i]:
                    es_marco_pag = True
            
            if es_proceso or es_marco_pag:
                print(f'RESULTADO -> PID: {pcb_pids[i]} | Nombre: {pcb_nombres[i]}')
                print(f'Marcos/Páginas ocupados: {pcb_marcos_usados[i]}')
                print(f'Tamaño real: {pcb_tamanos_kb[i]}KB')
                encontrado = True
                break
        
        if not encontrado:
            print('No se encontró ninguna coincidencia.')

    elif opcion == 4:
        print(f'\n{"-" * 5} Visualización de RAM {"-" * 5}')
        # Imprimir el vector estilo cadena
        mapa = "".join(lista_principal)
        print(f'Mapa: {mapa}')
        
        print('\nDetalle de Marcos:')
        # Mostrar los 25 marcos con su contenido
        for i in range(total_bloques):
            print(f'[M:{i} P:{i}] -> {lista_principal[i]}', end='\t')
            if (i + 1) % 5 == 0: print() # Formato de 5 en 5

    elif opcion == 5:
        salir = True

print("Simulación finalizada.")