import random

print(f'\n{"=" * 20} SimuRAM: Proyecto Final {"=" * 20}\n')

# 1) Configuración de Hardware [cite: 4, 5]
tamano_ram_kb = int(input('1) Escribe el tamaño de la RAM (KB): '))
tamano_marco_kb = int(input('2) Escribe el tamaño del marco (KB): '))
tamano_marco_bytes = tamano_marco_kb * 1024
total_bloques = tamano_ram_kb // tamano_marco_kb

# Inicialización de vectores [cite: 14, 30]
lista_ram = ["-" for _ in range(total_bloques)]
lista_vram = ["-" for _ in range(total_bloques)]

# PCB y Control [cite: 8, 16]
pcb_pids = []
pcb_paginas_info = [] 
pcb_ubicacion = [] # 'RAM' o 'VRAM' [cite: 30, 32]
pcb_estados = []   # X (Ejecución), R (Ready), W (Wait), E (End) [cite: 40, 49]
pid_automatico = 1 
contador_paginas_global = 0

salir = False
while not salir:
    libres_ram = lista_ram.count("-")
    libres_vram = lista_vram.count("-")

    print(f"\n[ RAM: {libres_ram} libres | VRAM: {libres_vram} libres ]")
    print(f'{"-" * 10} MENÚ  {"-" * 10}')
    print("1. Crear Proceso")
    print("2. Eliminar Proceso")
    print("3. Búsqueda de Procesos")
    print("4. Visualizar RAM / VRAM")
    print("5. Simular Ciclos")
    print("6. Salir")
    opcion = int(input('OPCIÓN: '))

    if opcion == 1:
        tamano_kb = int(input(f'Tamaño del proceso PID {pid_automatico} (KB): '))
        marcos_necesarios = (tamano_kb + tamano_marco_kb - 1) // tamano_marco_kb
        
        inicio_ram = -1
        i = 0
        while i <= total_bloques - marcos_necesarios:
            if all(lista_ram[i+k] == "-" for k in range(marcos_necesarios)):
                inicio_ram = i
                break
            i += 1

        if inicio_ram != -1:
            info_paginas = []
            for k in range(marcos_necesarios):
                m_act = inicio_ram + k
                lista_ram[m_act] = str(pid_automatico)
                est_pag = random.choice(["Heat", "Cold"])
                info_paginas.append({"id_p": contador_paginas_global, "marco": m_act, "errores": 0, "estado": est_pag})
                contador_paginas_global += 1
            pcb_pids.append(pid_automatico)
            pcb_ubicacion.append('RAM')
            pcb_estados.append('X') 
            print(f' PID {pid_automatico} creado en RAM.')
        else:
            inicio_vram = -1
            i = 0
            while i <= total_bloques - marcos_necesarios:
                if all(lista_vram[i+k] == "-" for k in range(marcos_necesarios)):
                    inicio_vram = i
                    break
                i += 1
            
            if inicio_vram != -1:
                info_paginas = []
                for k in range(marcos_necesarios):
                    m_act = inicio_vram + k
                    lista_vram[m_act] = str(pid_automatico)
                    est_pag = random.choice(["Heat", "Cold"])
                    info_paginas.append({"id_p": contador_paginas_global, "marco": m_act, "errores": 0, "estado": est_pag})
                    contador_paginas_global += 1
                pcb_pids.append(pid_automatico)
                pcb_ubicacion.append('VRAM')
                pcb_estados.append('W') 
                print(f'RAM LLENA: PID {pid_automatico} enviado a VRAM (Estado Wait).')
            else:
                print("ERROR: Memoria insuficiente.")
                continue

        pcb_paginas_info.append(info_paginas)
        pid_automatico += 1

    elif opcion == 2:
        pid_buscado = int(input("PID a eliminar: "))
        if pid_buscado in pcb_pids:
            idx = pcb_pids.index(pid_buscado)
            if pcb_ubicacion[idx] == 'RAM':
                for pag in pcb_paginas_info[idx]: lista_ram[pag["marco"]] = "-"
            else:
                for pag in pcb_paginas_info[idx]: lista_vram[pag["marco"]] = "-"
            pcb_pids.pop(idx); pcb_paginas_info.pop(idx); pcb_ubicacion.pop(idx); pcb_estados.pop(idx)
            print(f"PID {pid_buscado} eliminado.")
        else: print("PID no encontrado.")

    elif opcion == 3:
        bus = int(input("PID a buscar: "))
        off = int(input("Offset (Dirección Real): "))
        if bus in pcb_pids:
            i = pcb_pids.index(bus)
            print(f"Resultado: PID {pcb_pids[i]} | Ubicación: {pcb_ubicacion[i]} | Estado: {pcb_estados[i]}")
            if pcb_ubicacion[i] == 'RAM':
                p = pcb_paginas_info[i][0]
                df = (p['marco'] * tamano_marco_bytes) + off
                print(f"Dirección Real: ({p['marco']} * {tamano_marco_bytes}) + {off} = {df}")
        else: print("No encontrado.")

    elif opcion == 4:
        print(f'\nMAPA RAM (PID):  | {" | ".join(lista_ram)} |')
        print(f'MAPA VRAM (PID): | {" | ".join(lista_vram)} |')
        print("-" * 60)
        for i in range(len(pcb_pids)):
            print(f"PID: {pcb_pids[i]} | Ubicación: {pcb_ubicacion[i]} | Estado: {pcb_estados[i]}")

    elif opcion == 5:
        n = int(input("Número de ciclos a simular: "))
        for ciclo in range(n):
            print(f"\n{'='*10} INICIANDO CICLO {ciclo + 1} {'='*10}")
            i = 0
            while i < len(pcb_pids):
                # REPORTES PARA PROCESOS EN RAM [cite: 30, 32]
                if pcb_ubicacion[i] == 'RAM':
                    if random.random() < 0.30: # Probabilidad de cambio de estado [cite: 38, 41]
                        sub = random.random()
                        if sub < 0.60: # 60% a Ready (R) [cite: 40]
                            print(f"[EVENTO] PID {pcb_pids[i]}: Cambió de X -> R (Listo).")
                            pcb_estados[i] = 'R'
                        elif sub < 0.80: # 20% a Wait (W) - Mover a VRAM [cite: 40, 48]
                            m_nec = len(pcb_paginas_info[i])
                            ini_v = -1
                            for v in range(total_bloques - m_nec + 1):
                                if all(lista_vram[v+k] == "-" for k in range(m_nec)):
                                    ini_v = v; break
                            if ini_v != -1:
                                print(f"[EVENTO] PID {pcb_pids[i]}: Cambió de X -> W. Enviado a VRAM.")
                                for pag in pcb_paginas_info[i]: lista_ram[pag["marco"]] = "-"
                                for k in range(m_nec):
                                    lista_vram[ini_v + k] = str(pcb_pids[i])
                                    pcb_paginas_info[i][k]["marco"] = ini_v + k
                                pcb_ubicacion[i] = 'VRAM'; pcb_estados[i] = 'W'
                            else: print(f"[AVISO] PID {pcb_pids[i]}: No hay espacio en VRAM.")
                        else: # 20% a End (E) [cite: 40, 49]
                            print(f"[EVENTO] PID {pcb_pids[i]}: Ha finalizado su ejecución (E).")
                            for pag in pcb_paginas_info[i]: lista_ram[pag["marco"]] = "-"
                            pcb_pids.pop(i); pcb_paginas_info.pop(i); pcb_ubicacion.pop(i); pcb_estados.pop(i)
                            continue
                    else:
                        pcb_estados[i] = 'X' # 70% sigue en Ejecución [cite: 37]
                        # Gestión de errores por página 
                        for pag in pcb_paginas_info[i]:
                            if random.random() < 0.30: 
                                pag["errores"] += 1
                                print(f"[FALLO] PID {pcb_pids[i]} - Pág {pag['id_p']}: Error acumulado ({pag['errores']}/5).")
                            if pag["errores"] >= 5: # Sustitución 
                                print(f"[SUSTITUCIÓN] PID {pcb_pids[i]} - Pág {pag['id_p']}: Generar nueva pág y aviso.")
                                pag["errores"] = 0
                
                # REPORTES PARA PROCESOS EN VRAM [cite: 32, 48]
                elif pcb_ubicacion[i] == 'VRAM':
                    sub_prob = random.random()
                    if sub_prob < 0.60: # 60% intenta subir a RAM (R) [cite: 42]
                        m_nec = len(pcb_paginas_info[i])
                        ini_r = -1
                        for r in range(total_bloques - m_nec + 1):
                            if all(lista_ram[r+k] == "-" for k in range(m_nec)):
                                ini_r = r; break
                        
                        # Compactación si es necesario 
                        if ini_r == -1:
                            print(f"[SISTEMA] RAM fragmentada: Compactando para intentar subir PID {pcb_pids[i]}...")
                            temp = [m for m in lista_ram if m != "-"]
                            while len(temp) < total_bloques: temp.append("-")
                            lista_ram = temp
                            # Actualizar marcos en PCB tras compactar
                            for p_idx in range(len(pcb_pids)):
                                if pcb_ubicacion[p_idx] == 'RAM':
                                    primer_m = lista_ram.index(str(pcb_pids[p_idx]))
                                    for k_p in range(len(pcb_paginas_info[p_idx])):
                                        pcb_paginas_info[p_idx][k_p]["marco"] = primer_m + k_p
                            # Reintentar búsqueda
                            for r in range(total_bloques - m_nec + 1):
                                if all(lista_ram[r+k] == "-" for k in range(m_nec)):
                                    ini_r = r; break

                        if ini_r != -1:
                            print(f"[EVENTO] PID {pcb_pids[i]}: Subió de VRAM -> RAM (Estado Ready).")
                            for pag in pcb_paginas_info[i]: lista_vram[pag["marco"]] = "-"
                            for k in range(m_nec):
                                lista_ram[ini_r + k] = str(pcb_pids[i])
                                pcb_paginas_info[i][k]["marco"] = ini_r + k
                            pcb_ubicacion[i] = 'RAM'; pcb_estados[i] = 'R'
                        else: print(f"[AVISO] PID {pcb_pids[i]}: Sigue en VRAM, no cupo tras compactar.")
                    else: # 40% Finaliza desde VRAM (E) [cite: 43]
                        print(f"[EVENTO] PID {pcb_pids[i]}: Finalizó (E) directamente desde VRAM.")
                        for pag in pcb_paginas_info[i]: lista_vram[pag["marco"]] = "-"
                        pcb_pids.pop(i); pcb_paginas_info.pop(i); pcb_ubicacion.pop(i); pcb_estados.pop(i)
                        continue
                i += 1
        print("Ciclos completados.")

    elif opcion == 6: salir = True