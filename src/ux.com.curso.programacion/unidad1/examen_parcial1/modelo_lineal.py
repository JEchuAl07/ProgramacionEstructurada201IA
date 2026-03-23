#Diseñar un algoritmo que calcule el valor de Activación (Z) de una neurona simple antes de pasar por su función no lineal.

def calcular_activacion():
    # Solicitar al usuario que ingrese el peso y el valor del dato de entrada
    w = float(input("Ingrese el valor del peso: "))
    x = float(input("Ingrese el valor del dato de entrada: "))

    # Calcular la activación (Z) 
    z = w * x

    print(f"El valor de Activación es: {z}")

def main():
    print("Bienvenido al cálculo de Activación de una neurona simple")
    calcular_activacion()

if __name__ == "__main__":
    main()