import random

print(f'{"=" * 20} SimuRAM y VRAM {"=" * 20}')

# Configuración de Hardware
tamano_ram_kb = 100
tamano_marco_kb = 4
tamano_marco_bytes = 4096
total_bloques = tamano_ram_kb // tamano_marco_kb # 25 marcos

lista_ram = ["-" for _ in range(total_bloques)]
vram = [] # Lista para procesos en Memoria Virtual

# PCB y Control
pcb_pids = []
pcb_nombres = []
pcb_paginas_info = [] 
pcb_ubicacion = []
pid_automatico = 0
contador_paginas_global = 0

salir = False

while not salir:
    print(f"\n[ Páginas: {contador_paginas_global} | En RAM: {lista_ram.count('-')} marcos libres ]")
    opcion = int(input(f'''
{"-" * 10} MENÚ SISTEMA OPERATIVO {"-" * 10}
1. Crear Proceso (con Swapping a VRAM)
2. Eliminar Proceso
3. Buscar Proceso y Dirección Física
4. Visualizar RAM, VRAM y PCB
5. Simular Ciclos de Ejecución (1 o N ciclos)
6. Salir
OPCIÓN: '''))

    if opcion == 1:
        nombre = input('Nombre del proceso: ')
        if nombre in pcb_nombres:
            print("Error: El nombre ya existe.")
        else:
            tamano_kb = int(input('Tamaño en KB: '))
            marcos_necesarios = (tamano_kb + tamano_marco_kb - 1) // tamano_marco_kb
            
            if marcos_necesarios > total_bloques:
                print("Error: El proceso es más grande que toda la RAM.")
                continue

            # Intentar buscar espacio con Best-Fit
            def buscar_espacio():
                mejor_ini = -1
                mejor_tam = total_bloques + 1
                i = 0
                while i < total_bloques:
                    if lista_ram[i] == "-":
                        ini = i
                        tam = 0
                        while i < total_bloques and lista_ram[i] == "-":
                            tam += 1
                            i += 1
                        if tam >= marcos_necesarios and tam < mejor_tam:
                            mejor_tam = tam
                            mejor_ini = ini
                    else: i += 1
                return mejor_ini

            inicio = buscar_espacio()

            # LÓGICA DE SWAPPING (Si no cabe, mandar a VRAM)
            while inicio == -1 and len(pcb_nombres) > 0:
                # Buscar el primer proceso que esté en RAM para moverlo a VRAM
                idx_swap = -1
                for i in range(len(pcb_ubicacion)):
                    if pcb_ubicacion[i] == 'RAM':
                        idx_swap = i
                        break
                
                if idx_swap != -1:
                    nom_swap = pcb_nombres[idx_swap]
                    print(f"(!) RAM llena. Moviendo proceso '{nom_swap}' a VRAM...")
                    for x in range(total_bloques):
                        if lista_ram[x] == nom_swap:
                            lista_ram[x] = "-"
                    pcb_ubicacion[idx_swap] = 'VRAM'
                    inicio = buscar_espacio() # Reintentar buscar espacio
                else: break

            if inicio != -1:
                info_paginas = []
                for k in range(marcos_necesarios):
                    m_actual = inicio + k
                    lista_ram[m_actual] = nombre
                    info_paginas.append({
                        "id_p": contador_paginas_global,
                        "marco": m_actual,
                        "estado": random.choice(["Heat", "Cold"]),
                        "errores": 0
                    })
                    contador_paginas_global += 1
                
                pid_automatico += 1
                pcb_pids.append(pid_automatico)
                pcb_nombres.append(nombre)
                pcb_paginas_info.append(info_paginas)
                pcb_ubicacion.append('RAM')
                print(f'Proceso "{nombre}" (PID: {pid_automatico}) cargado en RAM.')
            else:
                print("Error crítico: No se pudo liberar espacio suficiente.")

    elif opcion == 2:
        nombre_del = input("Nombre a eliminar: ")
        if nombre_del in pcb_nombres:
            idx = pcb_nombres.index(nombre_del)
            if pcb_ubicacion[idx] == 'RAM':
                for pag in pcb_paginas_info[idx]:
                    lista_ram[pag["marco"]] = "-"
            pcb_nombres.pop(idx); pcb_pids.pop(idx); pcb_paginas_info.pop(idx); pcb_ubicacion.pop(idx)
            print("Proceso eliminado de la memoria.")

    elif opcion == 3:
        print("\n--- BÚSQUEDA ---")
        print("1) PID 2) Nombre 3) Marco 4) Página")
        sub = int(input("Opción: "))
        bus = input("Dato: ")
        off = int(input("Offset (0-4095): "))
        encontrado = False
        for i in range(len(pcb_nombres)):
            p_en = None
            if sub == 1 and bus == str(pcb_pids[i]): p_en = pcb_paginas_info[i][0]
            elif sub == 2 and bus == pcb_nombres[i]: p_en = pcb_paginas_info[i][0]
            elif sub in [3, 4]:
                for p in pcb_paginas_info[i]:
                    if sub == 3 and bus == str(p['marco']): p_en = p; break
                    if sub == 4 and bus == str(p['id_p']): p_en = p; break
            
            if p_en:
                if pcb_ubicacion[i] == 'VRAM':
                    print(f"El proceso {pcb_nombres[i]} está en VRAM. No tiene dirección física en RAM.")
                else:
                    df = (p_en['marco'] * tamano_marco_bytes) + off
                    print(f"Encontrado: {pcb_nombres[i]} | Dirección Física: ({p_en['marco']}*4096)+{off} = {df}")
                encontrado = True; break
        if not encontrado: print("No encontrado.")

    elif opcion == 4:
        print(f'\nMAPA RAM: |', end="")
        for c in lista_ram: print(f" {c} |", end="")
        print(f"\nPROCESOS EN VRAM: {[pcb_nombres[i] for i in range(len(pcb_nombres)) if pcb_ubicacion[i] == 'VRAM']}")
        print("-" * 50)
        for i in range(len(pcb_nombres)):
            print(f"PID: {pcb_pids[i]} | Nombre: {pcb_nombres[i]} | Ubicación: {pcb_ubicacion[i]}")

    elif opcion == 5:
        n_ciclos = int(input("¿Cuántos ciclos deseas simular?: "))
        for c in range(n_ciclos):
            print(f"\n--- Ejecutando Ciclo {c+1} ---")
            for i in range(len(pcb_nombres)):
                # Solo procesos en RAM ejecutan y generan errores
                if pcb_ubicacion[i] == 'RAM':
                    for pag in pcb_paginas_info[i]:
                        if random.random() < 0.5:
                            pag["errores"] += 1
                            print(f"(!) Error: {pcb_nombres[i]} Pág {pag['id_p']} (Total: {pag['errores']})")
                        pag["estado"] = random.choice(["Heat", "Cold"])
                        
                        if pag["errores"] >= 5:
                            print(f"Sustituyendo Página {pag['id_p']} por exceso de errores...")
                            contador_paginas_global = 0
                            pag["id_p"] = contador_paginas_global
                            pag["errores"] = 0
                            contador_paginas_global += 1

    elif opcion == 6:
        salir = True