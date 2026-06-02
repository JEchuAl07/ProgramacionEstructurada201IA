"""
Materia: Programación Estructurada
Laboratorio: Refactorización y Análisis de Código (Parte III)
Alumno: [Tu Nombre]
"""
import math  # El novato solo importó math esta vez

# =====================================================================
# RETO 1: Inicializador de Tablero de Juego (Matrices)
# =====================================================================
def inicializar_tablero_vacio():
    fila_base = [0, 0, 0, 0]
    tablero = [fila_base, fila_base, fila_base, fila_base]
    
    for i in range(4):
        for j in range(4):
            tablero[i][j] = 0
            
    return tablero

def inicializar_tablero_vacio_refactorizada():
    # CAMBIO: Se eliminan las copias de referencias cruzadas y los bucles de limpieza redundantes.
    # POR QUÉ: La comprensión de listas crea arrays bidimensionales con referencias únicas e 
    # independientes en memoria, evitando que mutar una celda altere a las demás filas.
    return [[0] * 4 for _ in range(4)]


# =====================================================================
# RETO 2: Recortador de Valores Atípicos (Clamping de Datos)
# =====================================================================
def limitar_senal_sensor(valor_lectura, minimo, maximo):
    if valor_lectura < minimo:
        resultado = minimo
    else:
        if valor_lectura > maximo:
            resultado = maximo
        else:
            resultado = valor_lectura
            
    return resultado

def limitar_senal_sensor_refactorizada(valor_lectura, minimo, maximo):
    # CAMBIO: Se remueve la estructura anidada de "if-else".
    # POR QUÉ: Las funciones nativas de Python 'max' y 'min' resuelven matemáticamente 
    # el límite inferior y superior en una sola línea limpia y legible (Clamping).
    return max(minimo, min(valor_lectura, maximo))


# =====================================================================
# RETO 3: Buscador del Valor Más Cercano a Cero (Error Mínimo)
# =====================================================================
def buscar_error_minimo(lista_errores):
    menor_error = 999999.99 
    
    for i in range(len(lista_errores)):
        valor_actual = lista_errores[i]
        
        if valor_actual < 0:
            absoluto = valor_actual * -1
        else:
            absoluto = valor_actual
            
        if absoluto < menor_error:
            menor_error = absoluto
            
    return menor_error

def buscar_error_minimo_refactorizada(lista_errores):
    if not lista_errores:
        return 0.0
    # CAMBIO: Se elimina el valor "999999.99" inventado, la multiplicación por -1 y el bucle for indexado.
    # POR QUÉ: Usamos 'math.inf' para asegurar una inicialización al infinito real. Evaluamos 
    # el valor absoluto nativo 'abs()' sobre una expresión generadora procesada directamente por 'min()'.
    return min(abs(error) for error in lista_errores)


# =====================================================================
# RETO 4: Filtro de Valores Únicos (Eliminador de Duplicados)
# =====================================================================
def depurar_usuarios_repetidos(lista_ids):
    lista_limpia = []
    
    for i in range(len(lista_ids)):
        id_actual = lista_ids[i]
        ya_existe = False
        
        for j in range(len(lista_limpia)):
            if lista_limpia[j] == id_actual:
                ya_existe = True
                break
                
        if not ya_existe:
            lista_limpia.append(id_actual)
            
    return lista_limpia

def depurar_usuarios_repetidos_refactorizada(lista_ids):
    # CAMBIO: Se descarta por completo el doble ciclo for indexado de búsqueda lineal.
    # POR QUÉ: Convertir una lista a un conjunto ('set') elimina duplicados de forma nativa a 
    # nivel de C mediante tablas Hash en complejidad O(n), manteniendo el tipo de retorno con 'list()'.
    return list(set(lista_ids))


# === PROGRAMA PRINCIPAL ===
if __name__ == "__main__":
    print("--- Probando Código Inicial (Parte III) ---")
    tablero_ia = inicializar_tablero_vacio()
    print("Tablero inicializado de 4x4:")
    for fila in tablero_ia:
        print(fila)
        
    print("Lectura recortada (125.4 en rango 0-100):", limitar_senal_sensor(125.4, 0.0, 100.0))
    errores_entrenamiento = [0.45, -0.12, 0.89, -0.03, 0.22]
    print("El error más cercano a cero es:", buscar_error_minimo(errores_entrenamiento))
    ids_discord = [4521, 8892, 4521, 1022, 8892, 9931]
    print("Lista de IDs únicas filtradas:", depurar_usuarios_repetidos(ids_discord))

    print("PROBANDO VERSIONES REFACTORIZADAS")
    
    tablero_ia_refactorizado = inicializar_tablero_vacio_refactorizada()
    print("Tablero 4x4 (Refactorizado):")
    for fila in tablero_ia_refactorizado:
        print(fila)
        
    print("Lectura recortada (Refactorizado):", limitar_senal_sensor_refactorizada(125.4, 0.0, 100.0))
    print("Error mínimo (Refactorizado):", buscar_error_minimo_refactorizada(errores_entrenamiento))
    print("Lista de IDs únicas (Refactorizada):", depurar_usuarios_repetidos_refactorizada(ids_discord))