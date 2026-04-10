#Calculo de radio de una esfera
import math

def volumen_esfera():
    radio = float(input("Ingrese el radio de la esfera en cm: "))
    volumen = (4/3) * math.pi * math.pow(radio, 3)
    print("El volumen de la esfera es :", volumen, "cm cúbicos")

def main():
    volumen_esfera()

if __name__ == "__main__":
    main()