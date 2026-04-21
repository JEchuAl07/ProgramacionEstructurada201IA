#Tabla de multiplicar del 1 al 15

def tabla_multiplicar():
    n = 15
    print("    ", end="") 
    for i in range(1, n + 1):
        print(f"{i:4}", end="")
    print("\n" + "----" * (n + 1))

    for i in range(1, n + 1):
        print(f"{i:2} |", end="")
    
        for j in range(1, n + 1):
            resultado = i * j
            print(f"{resultado:4}", end="")
    
        print()

def main():
    tabla_multiplicar()

if __name__ == "__main__":
    main()