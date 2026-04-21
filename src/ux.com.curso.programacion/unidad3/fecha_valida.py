# Funcion para determinar si la fecha es valida

def fecha_valida():
    dia=int(input("Ingrese el dia: "))
    mes=int(input("Ingrese el mes: "))
    año=int(input("Ingrese el año: "))

    if mes<=12 and mes>=1:
        if mes == 2:
            if dia <= 28 and dia >= 1:
                print("La fecha es valida")
            else:
                print("La fecha no es valida, verifique el dia")
        else:
            if dia <= 30 and dia >= 1:
                print("La fecha es valida")
            else:
                print("La fecha no es valida, verifique el dia")
    else:
        print("La fecha no es valida, verifique el mes")

def main():
    fecha_valida()

if __name__ == "__main__":
    main()