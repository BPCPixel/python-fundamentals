import json
import os
import math

# --- CÓDIGOS DE COLOR ANSI PARA APARIENCIA DE TERMINAL ---
C_VERDE = '\033[1;32m'
C_AZUL = '\033[1;34m'
C_BLANCO = '\033[1;37m'
C_ROJO = '\033[1;31m'
C_AMARILLO = '\033[1;33m'
C_CYAN = '\033[1;36m'
C_RESET = '\033[0m'

archivo_disco = "simulador_fs.json"
tamano_bloque = 1024  # Cada bloque representará 1024 bytes (1 KB)

print(f"{C_CYAN}=== INICIANDO SIMULADOR DE ARCHIVOS ===){C_RESET}")
print("1. Continuar donde lo dejé")
print("2. Empezar desde cero (Formatear sistema)")
opcion_inicio = input("Elige una opción (1/2): ")

if opcion_inicio == "2":
    if os.path.exists(archivo_disco):
        os.remove(archivo_disco)
        print(f"{C_AMARILLO}Sistema formateado correctamente.{C_RESET}")

# --- CARGA O INICIALIZACIÓN DEL SISTEMA ---
sistema = {}
if os.path.exists(archivo_disco):
    with open(archivo_disco, "r") as f:
        sistema = json.load(f)
else:
    if opcion_inicio == "1":
         print(f"{C_ROJO}No se encontró guardado previo. Creando sistema nuevo...{C_RESET}")
         
    # Estructura base corregida (la raíz también tiene "contenido")
    sistema = {
        "disco_maximo_bytes": 0,
        "disco_usado_bytes": 0,
        "siguiente_bloque": 1, # Los bloques empiezan en 1
        "usuarios": {},
        "fs": { 
            "tipo": "dir",
            "contenido": {
                "home": {
                    "tipo": "dir",
                    "contenido": {}
                }
            }
        }
    }
    
    # Configuración inicial del disco
    while True:
        try:
            tam_mb = float(input(f"{C_AMARILLO}Configuración inicial: Ingresa el tamaño del disco en MB: {C_RESET}"))
            sistema["disco_maximo_bytes"] = tam_mb * 1024 * 1024
            break
        except ValueError:
            print(f"{C_ROJO}Por favor, ingresa un número válido.{C_RESET}")

# --- SISTEMA DE LOGIN / REGISTRO ---
usuario_actual = ""

while usuario_actual == "":
    print(f"\n{C_CYAN}--- ACCESO AL SISTEMA ---{C_RESET}")
    if len(sistema["usuarios"]) == 0:
        print("No hay usuarios registrados. Debes registrar el primer usuario (Admin).")
        opcion_log = "2"
    else:
        print("1. Login")
        print("2. Registrar nuevo usuario")
        opcion_log = input("Elige una opción (1/2): ")

    if opcion_log == "2":
        nuevo_usr = input("Nuevo nombre de usuario: ")
        if nuevo_usr in sistema["usuarios"]:
            print(f"{C_ROJO}El usuario ya existe.{C_RESET}")
        else:
            nuevo_pass = input("Contraseña: ")
            sistema["usuarios"][nuevo_usr] = nuevo_pass
            # Crear su carpeta personal en /home (ruta corregida)
            sistema["fs"]["contenido"]["home"]["contenido"][nuevo_usr] = {"tipo": "dir", "contenido": {}}
            print(f"{C_VERDE}Usuario {nuevo_usr} registrado con éxito.{C_RESET}")
            usuario_actual = nuevo_usr
            
    elif opcion_log == "1":
        usr = input("Usuario: ")
        pwd = input("Contraseña: ")
        if usr in sistema["usuarios"] and sistema["usuarios"][usr] == pwd:
            print(f"{C_VERDE}Acceso concedido.{C_RESET}")
            usuario_actual = usr
        else:
            print(f"{C_ROJO}Usuario o contraseña incorrectos.{C_RESET}")

# --- PREPARACIÓN DEL ENTORNO (LA TERMINAL) ---
ruta_actual = f"/home/{usuario_actual}"
ejecutando = True

print(f"\nBienvenido {C_VERDE}{usuario_actual}{C_RESET}. Escribe 'exit' para guardar y salir.")

while ejecutando:
    # 1. RESOLVER EL PUNTERO DEL DIRECTORIO ACTUAL (Evita el KeyError)
    dir_actual_dict = sistema["fs"]
    if ruta_actual != "/":
        partes_ruta = ruta_actual.strip("/").split("/")
        for parte in partes_ruta:
            dir_actual_dict = dir_actual_dict["contenido"][parte]

    # 2. PROMPT ESTILO LINUX CON COLORES
    prompt = f"{C_VERDE}{usuario_actual}@simulador{C_RESET}:{C_AZUL}{ruta_actual}{C_RESET}$ "
    comando_crudo = input(prompt).strip()
    
    if not comando_crudo:
        continue
        
    partes_cmd = comando_crudo.split(" ")
    cmd = partes_cmd[0].lower()
    args = partes_cmd[1:]

    # --- COMANDO EXIT ---
    if cmd == "exit":
        with open(archivo_disco, "w") as f:
            json.dump(sistema, f, indent=4)
        print(f"{C_AMARILLO}Cambios guardados. Apagando simulador...{C_RESET}")
        ejecutando = False

    # --- COMANDO PWD ---
    elif cmd == "pwd":
        print(ruta_actual)

    # --- COMANDO LS (Con colores diferenciados) ---
    elif cmd == "ls":
        for nombre, datos in dir_actual_dict["contenido"].items():
            if datos["tipo"] == "dir":
                print(f"{C_AZUL}{nombre}/{C_RESET}")
            else:
                tam = datos.get("tamano", 0)
                perm = datos.get("permisos", "777")
                print(f"{C_BLANCO}{nombre}{C_RESET}\t{tam} Bytes\t{C_AMARILLO}[{perm}]{C_RESET}")

    # --- COMANDO MKDIR ---
    elif cmd == "mkdir":
        if len(args) == 0:
            print(f"{C_ROJO}Error: Falta el nombre del directorio.{C_RESET}")
        else:
            nombre_dir = args[0]
            if nombre_dir in dir_actual_dict["contenido"]:
                resp = input(f"{C_AMARILLO}El directorio ya existe. ¿Deseas sobreescribirlo y borrar su contenido? (s/n): {C_RESET}")
                if resp.lower() == 's':
                    dir_actual_dict["contenido"][nombre_dir] = {"tipo": "dir", "contenido": {}}
                    print(f"{C_VERDE}Directorio sobreescrito.{C_RESET}")
            else:
                dir_actual_dict["contenido"][nombre_dir] = {"tipo": "dir", "contenido": {}}

    # --- COMANDO TOUCH ---
    elif cmd == "touch":
        if len(args) == 0:
            print(f"{C_ROJO}Error: Falta el nombre del archivo.{C_RESET}")
        else:
            nombre_archivo = args[0]
            if nombre_archivo in dir_actual_dict["contenido"]:
                print(f"{C_ROJO}Error: El archivo ya existe.{C_RESET}")
            else:
                try:
                    tam_bytes = int(input(f"Tamaño estimado de '{nombre_archivo}' en Bytes: "))
                    if sistema["disco_usado_bytes"] + tam_bytes > sistema["disco_maximo_bytes"]:
                        print(f"{C_ROJO}ERROR: Memoria insuficiente en el disco.{C_RESET}")
                    else:
                        num_bloques = math.ceil(tam_bytes / tamano_bloque)
                        if num_bloques == 0: num_bloques = 1
                        
                        bloques_asignados = []
                        for _ in range(num_bloques):
                            bloques_asignados.append(sistema["siguiente_bloque"])
                            sistema["siguiente_bloque"] += 1
                            
                        sistema["disco_usado_bytes"] += tam_bytes
                        
                        dir_actual_dict["contenido"][nombre_archivo] = {
                            "tipo": "archivo",
                            "tamano": tam_bytes,
                            "bloques": bloques_asignados,
                            "permisos": "777",
                            "propietario": usuario_actual
                        }
                        print(f"{C_VERDE}Archivo creado. Bloques: {bloques_asignados}{C_RESET}")
                except ValueError:
                    print(f"{C_ROJO}Tamaño inválido.{C_RESET}")

    # --- COMANDO RMDIR / DEL ---
    elif cmd in ["rmdir", "del", "rm"]:
        if len(args) == 0:
            print(f"{C_ROJO}Error: Falta el nombre.{C_RESET}")
        else:
            nombre_obj = args[0]
            if nombre_obj not in dir_actual_dict["contenido"]:
                print(f"{C_ROJO}Error: No existe ese archivo o directorio.{C_RESET}")
            else:
                obj = dir_actual_dict["contenido"][nombre_obj]
                if obj.get("permisos") == "444" and obj.get("propietario") != "root":
                    print(f"{C_ROJO}Error: Archivo protegido (Permisos 444). Usa chmod.{C_RESET}")
                else:
                    if obj["tipo"] == "archivo":
                        sistema["disco_usado_bytes"] -= obj["tamano"]
                    del dir_actual_dict["contenido"][nombre_obj]
                    print(f"{C_VERDE}'{nombre_obj}' eliminado.{C_RESET}")

    # --- COMANDO CHMOD ---
    elif cmd == "chmod":
        if len(args) < 2:
            print(f"{C_AMARILLO}Uso: chmod [777 o 444] [nombre_archivo]{C_RESET}")
        else:
            permiso = args[0]
            nombre_obj = args[1]
            if permiso not in ["777", "444"]:
                print(f"{C_ROJO}El simulador solo acepta 777 (Todo) o 444 (Solo lectura).{C_RESET}")
            elif nombre_obj in dir_actual_dict["contenido"]:
                dir_actual_dict["contenido"][nombre_obj]["permisos"] = permiso
                print(f"{C_VERDE}Permisos de '{nombre_obj}' cambiados a {permiso}.{C_RESET}")
            else:
                print(f"{C_ROJO}Archivo no encontrado.{C_RESET}")

    # --- COMANDO CD ---
    elif cmd == "cd":
        if len(args) == 0:
            ruta_actual = f"/home/{usuario_actual}"
        else:
            destino = args[0]
            if destino == "..":
                if ruta_actual != "/":
                    partes = ruta_actual.strip("/").split("/")
                    partes.pop()
                    if len(partes) == 0:
                        ruta_actual = "/"
                    else:
                        ruta_actual = "/" + "/".join(partes)
            else:
                sub_partes = destino.split("/")
                ruta_temporal = ruta_actual
                dir_temporal_dict = dir_actual_dict
                error = False
                
                for p in sub_partes:
                    if p == "": continue
                    if p in dir_temporal_dict["contenido"] and dir_temporal_dict["contenido"][p]["tipo"] == "dir":
                        dir_temporal_dict = dir_temporal_dict["contenido"][p]
                        if ruta_temporal == "/":
                            ruta_temporal = f"/{p}"
                        else:
                            ruta_temporal = f"{ruta_temporal}/{p}"
                    else:
                        print(f"{C_ROJO}Error: La ruta '{p}' no existe o no es un directorio.{C_RESET}")
                        error = True
                        break
                
                if not error:
                    ruta_actual = ruta_temporal

    # --- COMANDO DESCONOCIDO ---
    else:
        print(f"{C_ROJO}Comando '{cmd}' no reconocido. Usa: ls, cd, pwd, mkdir, touch, del/rmdir, chmod, exit.{C_RESET}")