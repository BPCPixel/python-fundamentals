"""
Simulador de Sistema de Archivos Jerárquico (Árbol)
Autor: Lalo Téllez
"""

import random

# --- Configuración de RAM ---
almacenamiento_kb = int(input('Tamaño total de la RAM (KB): '))
tamano_bloque_kb = int(input('Tamaño de cada bloque (KB): '))
total_bloques = almacenamiento_kb // tamano_bloque_kb
memoria_ram = ["." for _ in range(total_bloques)]

class Nodo:
    def __init__(self, nombre, tipo, tamano=0, bloques=None):
        self.nombre = nombre
        self.tipo = tipo  # "Carpeta" o "Archivo"
        self.tamano = tamano
        self.bloques = bloques if bloques else []
        self.hijos = []  # Solo para carpetas

# El "Tronco" o Raíz del sistema
raiz = Nodo("/", "Carpeta")

def asignar_bloques(nombre_archivo, tam_kb):
    bloques_nec = (tam_kb + tamano_bloque_kb - 1) // tamano_bloque_kb
    libres = memoria_ram.count(".")
    
    if bloques_nec <= libres:
        posiciones = []
        contador = 0
        for i in range(total_bloques):
            if memoria_ram[i] == "." and contador < bloques_nec:
                memoria_ram[i] = nombre_archivo[0] # Usar inicial para el mapa
                posiciones.append(i)
                contador += 1
        return posiciones
    return None

def visualizar_arbol(nodo, nivel=0):
    prefijo = "  " * nivel + "|-- " if nivel > 0 else ""
    tipo_str = f"({nodo.tipo})" if nodo.tipo == "Carpeta" else f"[Archivo {nodo.tamano}KB]"
    print(f"{prefijo}{nodo.nombre} {tipo_str}")
    
    if nodo.tipo == "Carpeta":
        for hijo in nodo.hijos:
            visualizar_arbol(hijo, nivel + 1)

# --- Menú Principal ---
salir = False
while not salir:
    print("\n" + "="*40)
    print(f"SISTEMA DE ARCHIVOS (RAM Libre: {memoria_ram.count('.') * tamano_bloque_kb} KB)")
    print("="*40)
    opcion = int(input("""1. Crear Carpeta (Rama)
2. Crear Archivo (Hoja)
3. Visualizar Árbol
4. Salir
OPCIÓN: """))

    if opcion == 1:
        nombre = input("Nombre de la carpeta: ")
        # Por simplicidad se agregan a la raíz (Tronco)
        raiz.hijos.append(Nodo(nombre, "Carpeta"))
        print(f"Carpeta '{nombre}' creada.")

    elif opcion == 2:
        if not raiz.hijos:
            print("Error: Crea primero una carpeta (rama) para contener el archivo.")
            continue
            
        print("\nSeleccione la carpeta destino:")
        for i, h in enumerate(raiz.hijos):
            if h.tipo == "Carpeta":
                print(f"{i}. {h.nombre}")
        
        idx = int(input("Índice de carpeta: "))
        nombre = input("Nombre del archivo: ")
        tam = int(input("Tamaño (KB): "))
        
        bloques = asignar_bloques(nombre, tam)
        if bloques:
            nuevo_archivo = Nodo(nombre, "Archivo", tam, bloques)
            raiz.hijos[idx].hijos.append(nuevo_archivo)
            print(f"Archivo '{nombre}' guardado en '{raiz.hijos[idx].nombre}'.")
        else:
            print("Error: Espacio insuficiente en RAM.")

    elif opcion == 3:
        print("\n--- ESTRUCTURA DE ÁRBOL ---")
        visualizar_arbol(raiz)
        print("\nMAPA FÍSICO RAM:")
        print("".join([f"[{b}]" for b in memoria_ram]))

    elif opcion == 4:
        salir = True