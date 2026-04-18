#Clasificador de objetos en vision arificial

def clasificador():
    umbral_pequeño = 5
    umbtal_grande = 20

    dimension = float(input("Ingrese el tamaño del objeto en cm: "))
    volumen = dimension ** 3

    if dimension < 0:
        print("Error: Lectura inválida. Verifique el sensor.")
    elif dimension <= umbral_pequeño:
        print("Clasificación: Micro-componente (Grado A)")
    elif dimension <= umbtal_grande:
        print("Clasificación: Componente Estándar (Grado B)")
    else:
        print("Clasificación: Componente Industrial (Grado C)")
        print(f"Espacio requerido en contenedor: {volumen} cm3")
    
    print("Registro de inspección completado.")

def main():
    print("Bienvenido al sistema de clasificación de objetos.")
    clasificador()

if __name__ == "__main__":
    main()
