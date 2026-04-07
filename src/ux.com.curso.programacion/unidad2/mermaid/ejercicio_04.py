"""
Algoritmo de acumulación genérica
"""
def suma_acumulada():
    suma = 0
    while suma < 500:
        num = int(input("Ingresa un número a sumar"))
        suma += num
    return suma

def main():
    resultado = suma_acumulada()
    print("La suma acumulada es:", resultado)

if __name__  == "__main__":
    main()