#Función de division utilizando suma y resta

def division_suma_resta():
    divisor = int(input("Ingrese el divisor: ")) 
    dividendo = int(input("Ingrese el dividendo: "))
    contador = 0
    suma = divisor
    while suma <= dividendo:
        contador += 1
        suma += divisor
    residuo = dividendo - (contador * divisor)
    print(f"El resultado de la división es: {contador} y el residuo es: {residuo}")

def main():
    division_suma_resta()

if __name__ == "__main__":
    main()