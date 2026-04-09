"""
El objetivo de este ejercicio es crear un programa que capture, valide y normalice lecturas de un sensor utilizando operadores aritméticos y lógicos.
"""

def filtro_seguridad():
    limite_superior = 100
    limite_inferior = 0
    lectura = float(input("Ingrese la lectura del sensor termico: "))
    if lectura < limite_superior and lectura > limite_inferior:
        dato_normalizado = lectura / limite_superior
        print("Señal aceptada. Valor normalizado para el modelo:", dato_normalizado)
    else:
        print( "Error: Lectura fuera de rango. La señal se considera ruido.")
    
    print("Fin del proceso de filtrado de datos.")

def main():
    filtro_seguridad()

if __name__ == "__main__":
    main()