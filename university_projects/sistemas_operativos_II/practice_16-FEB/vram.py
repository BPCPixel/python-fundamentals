import random

print(f'{"=" * 20} SimuRAM: Gestión de Estados (X, R, W, E) {"=" * 20}')

# Configuración de Hardware
tamano_ram_kb = 100
tamano_marco_kb = 4
tamano_marco_bytes = 4096
total_bloques = tamano_ram_kb // tamano_marco_kb 

# Inicialización de vectores (RAM y VRAM)
lista_ram = ["-" for _ in range(total_bloques)]
lista_vram = ["-" for _ in range(total_bloques)]

# PCB y Control
pcb_pids = []
pcb_nombres = []
pcb_paginas_info = [] 
pcb_ubicacion = [] # 'RAM' o 'VRAM'
pcb_estados = []   # 'X' (Ejecución), 'R' (Ready), 'W' (Wait), 'E' (End)
pid_automatico = 0
contador_paginas_global = 0

salir = False
while not salir:
    libres_ram = lista_ram.count("-")
    libres_vram = lista_vram.count("-")

    print(f"\n[ RAM: {libres_ram} libres | VRAM: {libres_vram} libres ]")
    opcion = int(input(f'''
{"-" * 10} MENÚ SISTEMA OPERATIVO {"-" * 10}
1. Crear Proceso
2. Eliminar Proceso
3. Buscar Proceso
4. Visualizar RAM y VRAM
5. Simular Ciclos
6. Salir
OPCIÓN: '''))

    if opcion == 1:
        nombre = input('Nombre del proceso: ')
        if nombre in pcb_nombres:
            print("Error: El nombre ya existe.")
        else:
            tamano_kb = int(input('Tamaño en KB: '))
            marcos_necesarios = (tamano_kb + tamano_marco_kb - 1) // tamano_marco_kb
            
            # Intentar en RAM
            inicio_ram = -1
            mejor_t_r = total_bloques + 1
            i = 0
            while i < total_bloques:
                if lista_ram[i] == "-":
                    ini_t, tam_t = i, 0
                    while i < total_bloques and lista_ram[i] == "-":
                        tam_t += 1
                        i += 1
                    if tam_t >= marcos_necesarios and tam_t < mejor_t_r:
                        mejor_t_r, inicio_ram = tam_t, ini_t
                else: i += 1

            if inicio_ram != -1:
                info_paginas = []
                for k in range(marcos_necesarios):
                    m_act = inicio_ram + k
                    lista_ram[m_act] = nombre
                    info_paginas.append({"id_p": contador_paginas_global, "marco": m_act, "errores": 0})
                    contador_paginas_global += 1
                pcb_ubicacion.append('RAM')
                pcb_estados.append('X') # Inicia en Ejecución
                print(f'Proceso "{nombre}" en RAM (Estado: X).')
            else:
                # Intentar en VRAM
                inicio_vram = -1
                mejor_t_v = total_bloques + 1
                i = 0
                while i < total_bloques:
                    if lista_vram[i] == "-":
                        ini_t, tam_t = i, 0
                        while i < total_bloques and lista_vram[i] == "-":
                            tam_t += 1
                            i += 1
                        if tam_t >= marcos_necesarios and tam_t < mejor_t_v:
                            mejor_t_v, inicio_vram = tam_t, ini_t
                else: i += 1
                
                if inicio_vram != -1:
                    info_paginas = []
                    for k in range(marcos_necesarios):
                        m_act = inicio_vram + k
                        lista_vram[m_act] = nombre
                        info_paginas.append({"id_p": contador_paginas_global, "marco": m_act, "errores": 0})
                        contador_paginas_global += 1
                    pcb_ubicacion.append('VRAM')
                    pcb_estados.append('W') # Inicia en Espera
                    print(f'RAM llena. Proceso "{nombre}" en VRAM (Estado: W).')
                else:
                    print("Error: Sin espacio.")
                    continue

            pid_automatico += 1
            pcb_pids.append(pid_automatico)
            pcb_nombres.append(nombre)
            pcb_paginas_info.append(info_paginas)

    elif opcion == 2:
        nombre_del = input("Nombre a eliminar: ")
        if nombre_del in pcb_nombres:
            idx = pcb_nombres.index(nombre_del)
            if pcb_ubicacion[idx] == 'RAM':
                for pag in pcb_paginas_info[idx]: lista_ram[pag["marco"]] = "-"
            else:
                for pag in pcb_paginas_info[idx]: lista_vram[pag["marco"]] = "-"
            pcb_nombres.pop(idx); pcb_pids.pop(idx); pcb_paginas_info.pop(idx); pcb_ubicacion.pop(idx); pcb_estados.pop(idx)
            print(f"Proceso {nombre_del} eliminado.")
        else: print("No encontrado.")

    elif opcion == 3:
        bus = input("Proceso a buscar: ")
        off = int(input("Offset (0-4095): "))
        encontrado = False
        for i in range(len(pcb_nombres)):
            if bus == pcb_nombres[i] or bus == str(pcb_pids[i]):
                if pcb_ubicacion[i] == 'VRAM':
                    print(f"Proceso {pcb_nombres[i]} en VRAM (Estado: {pcb_estados[i]}).")
                else:
                    p = pcb_paginas_info[i][0]
                    df = (p['marco'] * tamano_marco_bytes) + off
                    print(f"En RAM (Estado: {pcb_estados[i]}): Dir. Física: ({p['marco']}*4096)+{off} = {df}")
                encontrado = True; break
        if not encontrado: print("No encontrado.")

    elif opcion == 4:
        print(f'\nMAPA RAM:  | {" | ".join(lista_ram)} |')
        print(f'MAPA VRAM: | {" | ".join(lista_vram)} |')
        print("-" * 60)
        for i in range(len(pcb_nombres)):
            print(f"PID: {pcb_pids[i]} | Proceso: {pcb_nombres[i]} | Ubicación: {pcb_ubicacion[i]} | Estado: {pcb_estados[i]}")

    elif opcion == 5:
        n = int(input("Número de ciclos: "))
        for ciclo in range(n):
            print(f"\n--- Ciclo {ciclo + 1} ---")
            i = 0
            while i < len(pcb_nombres):
                # LÓGICA PROCESOS EN RAM (X o R)
                if pcb_ubicacion[i] == 'RAM':
                    # Probabilidad de cambio de estado (30% según pizarrón)
                    if random.random() < 0.30:
                        sub_prob = random.random()
                        if sub_prob < 0.60: # 60% a Ready
                            pcb_estados[i] = 'R'
                            print(f"Proceso '{pcb_nombres[i]}' pasa a R (Ready).")
                        elif sub_prob < 0.80: # 20% a Wait (VRAM)
                            print(f"Proceso '{pcb_nombres[i]}' pasa a W. Moviendo a VRAM...")
                            m_nec = len(pcb_paginas_info[i])
                            # Buscar espacio en VRAM
                            ini_v = -1
                            j = 0
                            while j < total_bloques:
                                if lista_vram[j] == "-":
                                    it, tt = j, 0
                                    while j < total_bloques and lista_vram[j] == "-":
                                        tt += 1
                                        j += 1
                                    if tt >= m_nec: 
                                        ini_v = it
                                        break
                                else: j += 1
                            
                            if ini_v != -1:
                                for pag in pcb_paginas_info[i]: lista_ram[pag["marco"]] = "-"
                                for k in range(m_nec):
                                    lista_vram[ini_v + k] = pcb_nombres[i]
                                    pcb_paginas_info[i][k]["marco"] = ini_v + k
                                pcb_ubicacion[i] = 'VRAM'
                                pcb_estados[i] = 'W'
                            else:
                                print("VRAM llena, permanece en RAM en espera.")
                        else: # 20% a End (Liberar)
                            print(f"Proceso '{pcb_nombres[i]}' ha TERMINADO (E).")
                            for pag in pcb_paginas_info[i]: lista_ram[pag["marco"]] = "-"
                            pcb_nombres.pop(i); pcb_pids.pop(i); pcb_paginas_info.pop(i); pcb_ubicacion.pop(i); pcb_estados.pop(i)
                            continue
                    else:
                        pcb_estados[i] = 'X' # 70% sigue Ejecutando
                        # Simular errores de página (50% según libreta)
                        for pag in pcb_paginas_info[i]:
                            if random.random() < 0.5: pag["errores"] += 1
                            if pag["errores"] >= 5:
                                print(f"Sustitución en {pcb_nombres[i]} (Pág {pag['id_p']})")
                                pag["errores"] = 0
                
                # LÓGICA PROCESOS EN VRAM (W)
                elif pcb_ubicacion[i] == 'VRAM':
                    sub_prob = random.random()
                    if sub_prob < 0.60: # 60% intenta volver a RAM (R)
                        m_nec = len(pcb_paginas_info[i])
                        ini_r = -1
                        j = 0
                        while j < total_bloques:
                            if lista_ram[j] == "-":
                                it, tt = j, 0
                                while j < total_bloques and lista_ram[j] == "-":
                                    tt += 1
                                    j += 1
                                if tt >= m_nec:
                                    ini_r = it
                                    break
                            else: j += 1
                        
                        if ini_r != -1:
                            print(f"Subiendo '{pcb_nombres[i]}' a RAM (Estado: R).")
                            for pag in pcb_paginas_info[i]: lista_vram[pag["marco"]] = "-"
                            for k in range(m_nec):
                                lista_ram[ini_r + k] = pcb_nombres[i]
                                pcb_paginas_info[i][k]["marco"] = ini_r + k
                            pcb_ubicacion[i] = 'RAM'
                            pcb_estados[i] = 'R'
                        else:
                            print(f"'{pcb_nombres[i]}' intentó subir a RAM pero no cupo.")
                    else: # 40% termina desde VRAM (E)
                        print(f"Proceso '{pcb_nombres[i]}' TERMINADO (E) desde VRAM.")
                        for pag in pcb_paginas_info[i]: lista_vram[pag["marco"]] = "-"
                        pcb_nombres.pop(i); pcb_pids.pop(i); pcb_paginas_info.pop(i); pcb_ubicacion.pop(i); pcb_estados.pop(i)
                        continue
                i += 1

    elif opcion == 6:
        salir = True