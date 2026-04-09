"""
El objetivo es simular el cerebro de un asistente de voz que decide si ejecutar una acción basada en un porcentaje de certeza.
"""

def asistente_ia():
    umbral_alto = 80
    umbral_bajo = 40
    instruccion = input("Instrucción recibida: ")
    certeza = float(input("Porcentaje de certeza: "))

    if certeza > 95:
        print("Aviso: El modelo ha sido reforzado con éxito debido a la alta precisión.")
    elif certeza >= umbral_alto:
        print("Ejecutando acción:", instruccion, "Éxito")
    elif certeza >= umbral_bajo:
        print("Confianza insuficiente. ¿Se refiere a:", instruccion, "Por favor confirme.")
    else:
        print("Error 404: No pude entender la instrucción. Intente hablar más claro.")

    print("Sesión de procesamiento finalizada.")

def main():
    asistente_ia()

if __name__ == "__main__":
    main()