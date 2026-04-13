"""
Version 2 del clasificador de pixeles
"""

UMBRAL_ALTO = 0.7
UMBRAL_BAJO = 0.3

def clasificar_pixeles(intensidad):

    #Si la intensidad es menor a 0 o mayor a 1, es un valor inválido
    if intensidad < 0 or intensidad > 1:
        return print("Valor inválido. La intensidad debe estar entre 0 y 1.")
    
    if 0 <= intensidad < UMBRAL_BAJO:
        return print("Clasificacion (Fondo oscuro)")
    
    if UMBRAL_BAJO <= intensidad < UMBRAL_ALTO:
        return print("Clasificacion (Fondo gris)")
    
    if intensidad >= UMBRAL_ALTO:
        return print("Clasificacion (Objeto brillante)")

    print("Analisis de imagen finalizado.")

import os

def cargar_y_procesar(nombre_archivo):
    datos_limpios = []
    ruido_detectado = 0
    fondo_oscuro = 0
    fondo_gris = 0
    objeto_brillante = 0

    #Obtener la ruta del archivo
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(ruta_script, nombre_archivo)

    try:
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                #convertir la linea a un numero flotante
                valor_crudo = float(linea.strip())

                #Clasificar el pixel
                clasificacion = clasificar_pixeles(valor_crudo)

                #Agregar la logica de clasificacion
                if clasificacion is None:
                    ruido_detectado += 1
                else:
                    datos_limpios.append(valor_crudo)
                    if clasificacion == "Clasificacion (Fondo oscuro)":
                        fondo_oscuro += 1
                    elif clasificacion == "Clasificacion (Fondo gris)":
                        fondo_gris += 1
                    elif clasificacion == "Clasificacion (Objeto brillante)":
                        objeto_brillante += 1
        print("Resultados de clasificacion:")
        print(f"Ruido detectado: {ruido_detectado}")
        print(f"Fondo oscuro: {fondo_oscuro}")
        print(f"Fondo gris: {fondo_gris}")
        print(f"Objeto brillante: {objeto_brillante}")
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró en la ruta")

def main():
    cargar_y_procesar('lecturas_sensores.txt')

if __name__ == "__main__":
    main()
    