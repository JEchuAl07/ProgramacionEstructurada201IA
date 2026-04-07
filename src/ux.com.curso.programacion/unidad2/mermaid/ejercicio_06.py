"""
Fondo de ahorro
"""

def fondo_ahorro():
    meta = 1000
    ahorro=0
    while ahorro < meta:
        cantidad = int(input("¿Cuánto quieres ahorrar? "))
        ahorro += cantidad
    return ahorro

def main():
    resultado = fondo_ahorro()
    print("Meta alcanzada:", resultado)

if __name__ == "__main__":
    main()