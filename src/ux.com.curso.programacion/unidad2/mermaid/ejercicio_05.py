"""
Suma condicional
"""

def suma_condicional():
    suma = 0
    while True:
        num = int(input("Ingresa un número a sumar"))
        if num >= 10 and num <= 50:
            suma += num
        else:
            break
    return suma

def main():
    resultado = suma_condicional()
    print("La suma es:", resultado)