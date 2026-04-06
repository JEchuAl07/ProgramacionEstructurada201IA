# Generar una lista secuencial de los primeros N números impares (comenzando desde el 1).
def impares():
    numero = int(input("¿Cuántos impares quieres? "))
    c = 0
    n = 1

    while c < numero:
        print(n)
        n += 2
        c += 1

def main():
    impares()

if __name__ == "__main__":
    main()