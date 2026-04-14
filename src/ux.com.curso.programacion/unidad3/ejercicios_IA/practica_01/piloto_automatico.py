"""
Simulacion de sensores en piloto automatico
"""

def piloto_automatico():
    distancia = float(input("Ingrese la distancia al objeto más cercano (en metros): "))
    semaforo = input("Ingrese el estado del semáforo (rojo, amarillo, verde): ").lower()
    peaton = input("¿Hay peatones cruzando? (sí/no): ").lower()

    if distancia < 5 or peaton == "sí":
        print("¡FRENO DE EMERGENCIA ACTIVADO! Deteniendo el vehículo inmediatamente.")
    elif semaforo == "rojo":
        print("Estado: Detenido. Esperando luz verde.")
    elif semaforo == "amarillo":
        print("Estado: Precaución. Preparándose para detenerse.")
    elif semaforo == "verde":
        print("Estado: En movimiento. Todo despeejado para avanzar.")
    elif semaforo not in ["rojo", "amarillo", "verde"]:
        print("Error de lectura de sensores: Color de semáforo no reconocido.")
    
    print("Monitoreo de sensores constante...  Sistema activo.")

def main():
    piloto_automatico()

if __name__ == "__main__":
    main()

    