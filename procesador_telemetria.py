# ==========================================
# IMPORTACIÓN DE BIBLIOTECAS (Biblioteca Estándar)
# ==========================================
import sys

# ==========================================
# FUNCIONES GENERADAS POR IA (Audited & Verified)
# ==========================================

def limpiar_lecturas(lista_datos):
    lista_filtrada = []
    for lectura in lista_datos:
        if lectura >= 0.0 and lectura <= 100.0:
            lista_filtrada.append(lectura)
    return lista_filtrada


def calcular_alertas(lista_filtrada, umbral_critico):
    total_alertas = 0
    for lectura in lista_filtrada:
        if lectura < umbral_critico:
            total_alertas += 1
    return total_alertas


def generar_log_sistema(total_alertas):
    # Identificación de la plataforma de ejecución
    sistema_os = sys.platform.upper()
    
    # Evaluación del protocolo de seguridad mediante condicional tradicional
    if total_alertas > 3:
        accion = "ABORTAR"
    else:
        accion = "PERMITIDA"
        
    log_formateado = f"[{sistema_os}] Alertas críticas encontradas: {total_alertas}. Acción: {accion}"
    return log_formateado


# ==========================================
# PROGRAMA PRINCIPAL (Orquestación Manual)
# ==========================================
if __name__ == "__main__":
    # 1. Datos simulados de telemetría (con algunos errores de sensor)
    lecturas_raw = [12.5, -5.0, 88.2, 120.1, 1.2, 0.0, 45.6, 2.5]
    UMBRAL = 3.0
    
    print("=== SISTEMA DE TELEMETRÍA DE AGENTE AUTÓNOMO ===\n")
    
    # ORQUESTACIÓN ESTRUCTURADA (Paso de argumentos entre funciones)
    lecturas_limpias = limpiar_lecturas(lecturas_raw)
    alertas_detectadas = calcular_alertas(lecturas_limpias, UMBRAL)
    log_final = generar_log_sistema(alertas_detectadas)
    
    # Salida por pantalla del Log final del sistema
    print(log_final)


# ==========================================
# RETO DE EVALUACIÓN Y ENTREGABLE
# ==========================================
"""
EVIDENCIAS DE CONTROL DE CALIDAD Y AUDITORÍA:

1. EL PROMPT UTILIZADO:

"Actúa como un programador experto en Python Estructurado. Escribe el código de una 
función llamada [calcular_alertas]. Recibe como parámetro una lista de flotantes 
filtrados y un flotante con el umbral crítico, y debe retornar un número entero con 
el total de alertas detectadas que estén por debajo de dicho umbral. 
Restricciones: 
1. No utilices programación orientada a objetos. 
2. No utilices manejo de excepciones (nada de bloques try-except). 
3. Usa ciclos for tradicionales con append.
4. Gestiona los errores de datos usando condicionales if/else tradicionales."


2. TABLA DE PRUEBAS DE ESCRITORIO MANUAL (TRACE TABLE):
--------------------------------------------------------------------------------
Caso de Prueba Propuesto (Datos críticos / Todos erróneos o fuera de rango):
- lecturas_raw_test = [-10.5, 105.0, -0.1, 200.4]
- UMBRAL_TEST = 5.0

Paso a Paso del Flujo del Programa:

A) Ejecución de limpiar_lecturas([-10.5, 105.0, -0.1, 200.4]):
   - Inicializa lista_filtrada = []
   - Iteración 1: lectura = -10.5 -> Condición (-10.5 >= 0.0 y -10.5 <= 100.0) es Falsa. No hace nada.
   - Iteración 2: lectura = 105.0 -> Condición (105.0 >= 0.0 y 105.0 <= 100.0) es Falsa. No hace nada.
   - Iteración 3: lectura = -0.1  -> Condición (-0.1 >= 0.0 y -0.1 <= 100.0) es Falsa. No hace nada.
   - Iteración 4: lectura = 200.4 -> Condición (200.4 >= 0.0 y 200.4 <= 100.0) es Falsa. No hace nada.
   - Retorna: lista_filtrada = []

B) Ejecución de calcular_alertas([], 5.0):
   - Inicializa total_alertas = 0
   - El ciclo for sobre la lista vacía no realiza ninguna iteración.
   - Retorna: total_alertas = 0

C) Ejecución de generar_log_sistema(0):
   - sistema_os toma el valor de la plataforma (ej. 'WIN32' o 'LINUX').
   - Evalúa condición: total_alertas > 3 -> (0 > 3) es Falso.
   - Asigna: accion = "PERMITIDA"
   - Retorna: "[WIN32] Alertas críticas encontradas: 0. Acción: PERMITIDA"


3. AUDITORÍA DE CÓDIGO:
--------------------------------------------------------------------------------
¿La IA intentó utilizar alguna función, biblioteca externa o sintaxis avanzada?

Sí. En la primera interacción para la función 'limpiar_lecturas', la IA generó 
el filtrado utilizando una "Comprensión de Listas" con la siguiente sintaxis:
return [lectura for lectura in lista_datos if 0.0 <= lectura <= 100.0]

Modificación aplicada:
Se reformuló el prompt agregando la restricción explícita: "No utilices comprensión 
de listas , estructura el bucle for de forma tradicional usando 
el método .append() dentro del bloque condicional". Con esto, la IA corrigió su 
salida a la estructura clásica que se observa en el script final.
"""