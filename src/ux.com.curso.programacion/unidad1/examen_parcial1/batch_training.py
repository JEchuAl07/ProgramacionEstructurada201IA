#Diseñar un algoritmo que simule el proceso de alimentación de datos a una Red Neuronal

def alimentar_red_neuronal():
    vram=0  #variable para almacenar el consumo de memoria de la VRAM
    while vram < 2500:
        lotes_de_tensores=int(input("Ingrese el tamaño de lotes de tensores (MB): ")) #variable para almacenar el tamaño de los lotes de tensores que se van a alimentar a la red neuronal
        vram = vram + lotes_de_tensores

    print("El consumo de total acumulado ha llegado a", vram, "MB, por lo que ha alcanzado el límite de seguridad, no se pueden alimentar más datos a la red neuronal.")

def main():
    print("Bienvenido al proceso de alimentación de datos a una Red Neuronal")
    alimentar_red_neuronal()

if __name__ == "__main__":
    main()