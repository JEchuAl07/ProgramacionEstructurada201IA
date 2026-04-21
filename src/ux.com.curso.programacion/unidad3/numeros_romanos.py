#Conversor a numeros romanos menores o iguales a 3000

def romanos():
    mapeo = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    numero = int(input("Ingrese un número entero menor o igual a 3000: "))
    
    resultado = ""
    for valor, simbolo in mapeo:
        while numero >= valor:
            resultado += simbolo
            numero -= valor
    print(resultado)

def main():
    romanos()

if __name__ == "__main__":
    main()