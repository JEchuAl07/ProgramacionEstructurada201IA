# Ejercicio dias de la semana con match

def dias_semana():
    print("--Ejercicio de días de la semana--")
    opcion = input("Ingresa una opcion (1-7) ")

    match opcion:
        case "1":
            print("Lunes")
        case "2":
            print("Martes")
        case "3":
            print("Miércoles")
        case "4":   
            print("Jueves")
        case "5":
            print("Viernes")
        case "6":
            print("Sábado")
        case "7":
            print("Domingo")
        case _:
            print("Opción no válida")

def main():
    dias_semana()

if __name__ == "__main__":
    main()