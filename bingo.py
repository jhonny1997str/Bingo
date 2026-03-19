import random

def generar_tabla_completa():
    """Genera una tabla de Bingo con el formato estándar 5x5"""
    return {
        'B': random.sample(range(1, 16), 5),
        'I': random.sample(range(16, 31), 5),
        'N': random.sample(range(31, 46), 5),
        'G': random.sample(range(46, 61), 5),
        'O': random.sample(range(61, 76), 5)
    }

def imprimir_registro(tablas):
    print("\n" + "="*40)
    print("REGISTRO DE TABLAS DEL SISTEMA")
    print("="*40)
    for i in range(1, 6):
        nombre = f"TABLA #{i}"
        t = tablas[nombre]
        print(f"\n>>> {nombre}:")
        print("  B   I   N   G   O")
        for f in range(5):
            fila = [str(t[letra][f]).rjust(2) for letra in 'BINGO']
            print(" " + "  ".join(fila))
    print("\n" + "="*40 + "\n")

def jugar_bingo_personalizado():
    # 1. Crear las 5 tablas fijas
    tablas = {f"TABLA #{i}": generar_tabla_completa() for i in range(1, 6)}
    
    # Mostrar todas las tablas para tu control
    imprimir_registro(tablas)

    # 2. Definir objetivos específicos
    t1_letra_n = set(tablas["TABLA #1"]['N'])
    
    t2_ing = set()
    for letra in ['I', 'N', 'G']:
        t2_ing.update(tablas["TABLA #2"][letra])

    # 3. Construir el bombo controlado
    # Primero: Números para que Tabla 1 complete la N
    bloque_1 = list(t1_letra_n)
    random.shuffle(bloque_1)

    # Segundo: Números que le faltan a Tabla 2 para completar I-N-G
    bloque_2 = list(t2_ing - t1_letra_n)
    random.shuffle(bloque_2)

    # Tercero: El resto de números del 1 al 75
    ya_usados = set(bloque_1) | set(bloque_2)
    bloque_3 = list(set(range(1, 76)) - ya_usados)
    random.shuffle(bloque_3)

    bombo_final = bloque_1 + bloque_2 + bloque_3

    # 4. Ejecución del sorteo
    balotas_fuera = set()
    gano_t1 = False
    gano_t2 = False

    print("--- INICIA EL SORTEO CONTROLADO ---\n")
    
    for i, num in enumerate(bombo_final, 1):
        balotas_fuera.add(num)
        
        # Determinar letra
        letra = 'B' if num <= 15 else 'I' if num <= 30 else 'N' if num <= 45 else 'G' if num <= 60 else 'O'
        print(f"Balota {i}: [ {letra} - {num} ]")

        # Verificar Ganador 1 (Letra N)
        if not gano_t1:
            if t1_letra_n.issubset(balotas_fuera):
                print(f"\n¡¡ LA TABLA 1 GANO LA LETRA !! (Número: {num})\n")
                gano_t1 = True

        # Verificar Ganador 2 (Medio Cartón I-N-G)
        if gano_t1 and not gano_t2:
            if t2_ing.issubset(balotas_fuera):
                print(f"\n¡¡ LA TABLA 2 GANO EL MEDIO CARTON LLENO !! (Número: {num})\n")
                gano_t2 = True
                break # Terminamos el juego aquí

    print("--- FIN DEL JUEGO REGISTRADO ---")

if __name__ == "__main__":
    jugar_bingo_personalizado()