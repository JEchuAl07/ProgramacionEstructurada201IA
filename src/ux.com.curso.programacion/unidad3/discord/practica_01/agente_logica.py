
# hola

"""
Funcion que recibe un texto y decide que responder.
implementa programacion esrtucturada pura.
"""

def procesar_pregunta(mensaje_usuario):
    #1.- Normaliazcion (paso fundamental en IA)
    mensaje = mensaje_usuario.lower().strip()
    #2.- Base de conocimientos (diccionario)
    conocimientos = {
    #conceptos de estructura de control
        "if": "La sentencia if es un condicional. permite que el programa tome decisiones basandose en una condicion boolenana",
        "for": "El bucle for se utiliza para iterar sobre una secuencia (como una lista o un rango) y ejecutar un bloque de codigo varias veces",
        "while": "El bucle while se ejecuta mientras una condicion sea verdadera. es util para repetir un bloque de codigo hasta que se cumpla una condicion",
        "while not": "El bucle while not se ejecuta mientras una condicion sea falsa. es util para repetir un bloque de codigo hasta que se cumpla una condicion",
    #Tipos de datos
        "int": "Representa numeros enteros, como 1, 2, 3, no tiene parte decimal",
        "float": "Representa numeros con parte decimal, como 3.14 o 0.001",
        "str": "Representa cadenas de texto, como 'hola' o 'programacion'",
        "bool": "Representa valores de verdad, como True o False",
    #Funciones y modularidad
        "def": "Es la palabra reservada para definir una funcion en python",
        "return": "Se utiliza para devolver un valor desde una funcion",
        "import": "Se utiliza para importar modulos o librerias en python",
        "lambda": "Es una funcion anonima, es decir, una funcion sin nombre que se define en una sola linea",
    #operadores y sintaxis
        "print": "Es una funcion incorporada en python que se utiliza para mostrar informacion en la consola",
        "=": "Es el operador de asignacion, se utiliza para asignar un valor a una variable",
        "==": "Es el operador de igualdad, se utiliza para comparar dos valores y devuelve True si son iguales y False si no lo son",
        "+": "Es el operador de suma, se utiliza para sumar numeros o concatenar cadenas de texto",
        "-": "Es el operador de resta, se utiliza para restar numeros",
        "*": "Es el operador de multiplicacion, se utiliza para multiplicar numeros",
    }
    #3.- Logica de busqueda
    for clave in conocimientos:
            if clave in mensaje:
                return conocimientos[clave]

    #3.- Busqueda en la base de conocimientos
    if mensaje in conocimientos:
        return conocimientos[mensaje]
    else:
        return "Lo siento, no entiendo esa pregunta."

def main():
    print("Bienvenido al agente de logica. Preguntame sobre conceptos de programacion.")
    while True:
        pregunta = input("Tu pregunta: ")
        if pregunta.lower() == "salir":
            print("Adios!")
            break
        respuesta = procesar_pregunta(pregunta)
        print("Respuesta:", respuesta)
    
    
#prueba locar (offline)
if __name__ == "__main__":
    main()