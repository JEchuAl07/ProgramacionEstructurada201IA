#Recomendador de peliculas basado en genero y edad del usuario

def obtener_recomendacion(edad, genero):
    peliculas_accion=["Mad Max", "John Wick", "Inception"]
    peliculas_comedia=["Toy story", "Minions", "Free guy"]
    peliculas_terror=["Saw", "It", "El conjuro"]
   
    if edad < 13 and genero == "accion" or genero == "terror":
        print("Nota: Debido a tu edad, hemos ajustado la recomendación a contenido apto para todo público.")
        print("Recomendacion: Peliculas de comedia")
        print(peliculas_comedia)
    elif edad < 13 and genero == "comedia":
        print("Recomendacion: Peliculas de comedia")
        print(peliculas_comedia)
    else:
        print("Recomendacion: Peliculas de", genero)
        if genero == "accion":
            print(peliculas_accion)
        elif genero == "terror":
            print(peliculas_terror)

def main():
    print("Bienvenido al recomendador de peliculas. Responde las siguientes preguntas para obtener una recomendacion.")
    edad = int(input("Ingrese su edad: "))
    genero = input("Ingrese el genero de pelicula que le gusta (accion, comedia, terror): ").lower().strip()
    obtener_recomendacion(edad, genero)

if __name__ == "__main__":
    main()