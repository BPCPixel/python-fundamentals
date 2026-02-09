import random

print(f'{"=" * 20} Simulación de RAM con Direccionamiento {"=" * 20}')

# Configuración inicial
tamano_ram_kb = 100
tamano_marco_kb = 4
byte_por_kb = 1024
tamano_marco_bytes = tamano_marco_kb * byte_por_kb # 4096 bytes
total_bloques = tamano_ram_kb // tamano_marco_kb

lista_principal = ["-" for _ in range(total_bloques)]

# PCB y Control de Errores
pcb_pids = []
pcb_nombres = []
pcb_tamanos_kb = []
pcb_marcos_usados = []
fallos_pagina = 0  # Contador de errores de página

pid_automatico = 0
salir = False

while not salir:
    print(f"\n[ Fallos de Página acumulados: {fallos_pagina}/5 ]")
    opcion = int(input(f'''
{"-" * 10} MENÚ {"-" * 10}
1. Crear proceso (Asignación y Dirección Física)
2. Eliminar proceso
3. Buscar proceso
4. Visualizar RAM
5. Salir
OPCIÓN: '''))

    if opcion == 1:
        nombre = input('Nombre del proceso: ')
        tamano_solicitado = int(input('Tamaño en KB: '))
        marcos_necesarios = (tamano_solicitado + tamano_marco_kb - 1) // tamano_marco_kb
        
        # Búsqueda de espacio (Best-Fit)
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
                if tamano_hueco >= marcos_necesarios and tamano_hueco < mejor_tamano_hueco:
                    mejor_tamano_hueco = tamano_hueco
                    mejor_inicio = inicio_hueco
            else:
                i += 1

        # Lógica de Sustitución si no hay espacio
        if mejor_inicio == -1:
            fallos_pagina += 1
            print(f"¡Fallo de página! No hay espacio contiguo. Error #{fallos_pagina}")
            
            if fallos_pagina >= 5:
                print("Se alcanzó el límite de 5 errores. Sustituyendo primer proceso (FIFO)...")
                if len(pcb_nombres) > 0:
                    # Sacamos el primero que entró
                    nombre_viejo = pcb_nombres[0]
                    for x in range(total_bloques):
                        if lista_principal[x] == nombre_viejo:
                            lista_principal[x] = "-"
                    pcb_pids.pop(0); pcb_nombres.pop(0); pcb_tamanos_kb.pop(0); pcb_marcos_usados.pop(0)
                    fallos_pagina = 0 # Reiniciar contador tras sustituir
                    print(f"Proceso {nombre_viejo} expulsado. Intente crear el nuevo proceso otra vez.")
                else:
                    print("No hay procesos para sustituir.")
        else:
            # Asignación exitosa
            indices = []
            for k in range(marcos_necesarios):
                lista_principal[mejor_inicio + k] = nombre
                indices.append(mejor_inicio + k)
            
            # Cálculo de Dirección Física (usando el último marco asignado como el ejemplo del profe)
            ultimo_marco = indices[-1]
            offset_aleatorio = random.randint(0, 4095)
            # FÓRMULA: (Marco * 4096) + Offset
            dir_fisica = (ultimo_marco * tamano_marco_bytes) + offset_aleatorio
            
            pid_automatico += 1
            pcb_pids.append(pid_automatico)
            pcb_nombres.append(nombre)
            pcb_tamanos_kb.append(tamano_solicitado)
            pcb_marcos_usados.append(indices)
            
            print(f"\nProceso {nombre} asignado en Marcos: {indices}")
            print(f"Dirección Física Calculada: ({ultimo_marco})({tamano_marco_bytes}) + {offset_aleatorio} = {dir_fisica}")

    elif opcion == 2:
        dato = input('PID o Nombre a eliminar: ')
        idx = -1
        for i in range(len(pcb_nombres)):
            if dato == pcb_nombres[i] or dato == str(pcb_pids[i]):
                idx = i; break
        if idx != -1:
            nom = pcb_nombres[idx]
            for i in range(total_bloques):
                if lista_principal[i] == nom: lista_principal[i] = "-"
            pcb_pids.pop(idx); pcb_nombres.pop(idx); pcb_tamanos_kb.pop(idx); pcb_marcos_usados.pop(idx)
            print("Eliminado.")

    elif opcion == 3:
        busqueda = input('Buscar PID, Nombre o Marco: ')
        for i in range(len(pcb_nombres)):
            if busqueda == pcb_nombres[i] or busqueda == str(pcb_pids[i]) or (busqueda.isdigit() and int(busqueda) in pcb_marcos_usados[i]):
                print(f"PID: {pcb_pids[i]} | Nombre: {pcb_nombres[i]} | Marcos: {pcb_marcos_usados[i]}")
                break

    elif opcion == 4:
        print(f"\nMapa RAM: {''.join(lista_principal)}")
        for i in range(total_bloques):
            print(f"[M:{i}]->{lista_principal[i]}", end="\t")
            if (i + 1) % 5 == 0: print()

    elif opcion == 5:
        salir = True