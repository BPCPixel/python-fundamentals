import random

print(f'{"=" * 20} Simulación de RAM: Gestión Avanzada de Memoria {"=" * 20}')

# Configuración de Hardware
tamano_ram_kb = 100
tamano_marco_kb = 4
tamano_marco_bytes = 4096
total_bloques = tamano_ram_kb // tamano_marco_kb # 25 marcos

lista_principal = ["-" for _ in range(total_bloques)]

# PCB y Control
pcb_pids = []
pcb_nombres = []
pcb_paginas_info = [] 
pid_automatico = 0
contador_paginas_global = 0

salir = False

while not salir:
    print(f"\n[ Siguiente ID de Página Única: {contador_paginas_global} ]")
    opcion = int(input(f'''
{"-" * 10} MENÚ SISTEMA OPERATIVO {"-" * 10}
1. Crear Proceso
2. Eliminar Proceso
3. Buscar Proceso (Submenú)
4. Visualizar RAM y PCB (Detallado)
5. Simular Ciclos de Ejecución (Generar Errores)
6. Salir
OPCIÓN: '''))

    if opcion == 1:
        nombre = input('Nombre del proceso: ')
        if nombre in pcb_nombres:
            print("Error: El nombre ya existe.")
        else:
            tamano_kb = int(input('Tamaño en KB: '))
            marcos_necesarios = (tamano_kb + tamano_marco_kb - 1) // tamano_marco_kb
            
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

            if mejor_inicio != -1:
                info_paginas_proceso = []
                for k in range(marcos_necesarios):
                    marco_actual = mejor_inicio + k
                    lista_principal[marco_actual] = nombre
                    
                    info_paginas_proceso.append({
                        "id_pagina": contador_paginas_global,
                        "marco": marco_actual,
                        "estado": random.choice(["Heat", "Cold"]),
                        "errores": 0
                    })
                    contador_paginas_global += 1
                
                pid_automatico += 1
                pcb_pids.append(pid_automatico)
                pcb_nombres.append(nombre)
                pcb_paginas_info.append(info_paginas_proceso)
                print(f'Proceso "{nombre}" cargado con PID: {pid_automatico}.')
            else:
                print("Error: Espacio insuficiente.")

    elif opcion == 2:
        nombre_del = input("Nombre a eliminar: ")
        if nombre_del in pcb_nombres:
            idx = pcb_nombres.index(nombre_del)
            for pag in pcb_paginas_info[idx]:
                lista_principal[pag["marco"]] = "-"
            pcb_nombres.pop(idx); pcb_pids.pop(idx); pcb_paginas_info.pop(idx)
            print("Proceso eliminado.")

    elif opcion == 3:
        print("\n--- SUBMENÚ DE BÚSQUEDA ---")
        print("1) Por PID")
        print("2) Por Nombre")
        print("3) Por Marco")
        print("4) Por Página Única")
        sub_opcion = int(input("Seleccione criterio: "))
        
        busqueda = input("Ingrese el dato a buscar: ")
        offset = int(input('Escribe el valor del Offset para el cálculo físico (0-4095): '))
        
        encontrado = False
        for i in range(len(pcb_nombres)):
            pag_encontrada = None
            
            if sub_opcion == 1 and busqueda == str(pcb_pids[i]):
                pag_encontrada = pcb_paginas_info[i][0]
            elif sub_opcion == 2 and busqueda == pcb_nombres[i]:
                pag_encontrada = pcb_paginas_info[i][0]
            elif sub_opcion == 3 or sub_opcion == 4:
                for p in pcb_paginas_info[i]:
                    if sub_opcion == 3 and busqueda == str(p['marco']):
                        pag_encontrada = p; break
                    if sub_opcion == 4 and busqueda == str(p['id_pagina']):
                        pag_encontrada = p; break
            
            if pag_encontrada:
                marco = pag_encontrada['marco']
                dir_fisica = (marco * tamano_marco_bytes) + offset
                print(f"\n[ RESULTADO ]")
                print(f"Proceso: {pcb_nombres[i]} | PID: {pcb_pids[i]}")
                print(f"Página ID: {pag_encontrada['id_pagina']} | Marco RAM: {marco}")
                print(f"Fórmula Física: ({marco} * {tamano_marco_bytes}) + {offset} = {dir_fisica}")
                encontrado = True
                break
        if not encontrado: print("No se encontró ninguna coincidencia.")

    elif opcion == 4:
        print(f'\nMapa RAM (25 espacios):')
        # Visualización mejorada del vector con PID
        print("|", end="")
        for celda in lista_principal:
            if celda == "-":
                print("  -  |", end="")
            else:
                # Buscar el PID del proceso que ocupa la celda
                idx = pcb_nombres.index(celda)
                pid = pcb_pids[idx]
                print(f" {celda}({pid}) |", end="")
        print("\n" + "-" * 130)
        
        for i in range(len(pcb_nombres)):
            print(f"Proceso: {pcb_nombres[i]} | PID: {pcb_pids[i]}")
            for pag in pcb_paginas_info[i]:
                print(f"  [ID Pág: {pag['id_pagina']}] Marco: {pag['marco']} | {pag['estado']} | Errores: {pag['errores']}")

    elif opcion == 5:
        print("\n--- Ejecutando Ciclo de CPU ---")
        for i in range(len(pcb_nombres)):
            for pag in pcb_paginas_info[i]:
                if random.random() < 0.5:
                    pag["errores"] += 1
                
                if pag["errores"] >= 5:
                    print(f"!!! Pág {pag['id_pagina']} llegó a 5 errores. Sustituyendo...")
                    contador_paginas_global = 0 
                    pag["id_pagina"] = contador_paginas_global
                    pag["errores"] = 0
                    contador_paginas_global += 1

    elif opcion == 6:
        salir = True