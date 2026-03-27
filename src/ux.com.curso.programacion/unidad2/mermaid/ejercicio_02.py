
def factorial():
    factorial = 1
    i = 1
    n= int(input("Ingrese un número entero: "))
    while i <= n:
        factorial *= i
        i += 1
    return factorial

def main():
    resultado = factorial()
    print(f"El factorial del número ingresado es: {resultado}")

if __name__ == "__main__":
    main()