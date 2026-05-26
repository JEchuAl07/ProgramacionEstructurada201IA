def par_impar(numero):
    if numero % 2 == 0:
        return "Weird"
    else:
        if numero >=2 and numero <= 5:
            return "Not Weird"
        elif numero >= 6 and numero <= 20:
            return "Weird"
        elif numero > 20:
            return "Not Weird"
        
def main():
    n = int(input("Ingrese un número entero: "))
    resultado = par_impar(n)
    print(resultado)

if __name__ == "__main__":
    main()