import math

#demostracion el uso de funciones de math

def mostrar_funciones_math():
    #crear una variable
    numero = 20

    sen_x = math.sin(numero)
    cos_x = math.cos(numero)

    print("Seno de ", numero, " es: ", sen_x)
    print("Coseno de ", numero, " es: ", cos_x)

    resultado = sen_x ** 2 + cos_x ** 2

    print("El resultado de sen^2 + cos^2 es: ", resultado)

def main():
    mostrar_funciones_math()

if __name__ == "__main__":
    main()

