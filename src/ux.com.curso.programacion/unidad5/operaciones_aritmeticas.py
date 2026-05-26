def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    return suma, resta, multiplicacion

def main():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    resultado = operaciones(a, b)
    print(f"Suma: {resultado[0]}, Resta: {resultado[1]}, Multiplicación: {resultado[2]}")

if __name__ == "__main__":
    main()