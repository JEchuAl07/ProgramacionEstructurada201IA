"""
Clasificador de intenciones
"""

import datetime
ahora = datetime.datetime.now()

def clasificar_intencion():
    nombre_asistente = "IA-UX"
    frase = input("Hola, soy " + nombre_asistente + ". ¿En qué puedo ayudarte? ").lower()
    if "hola" in frase or "buenos dias" in frase:
        respuesta = "¡Hola! Soy tu asistente. Es un gusto saludarte."
    elif "clima" in frase:
        respuesta = "Consultando el servicio meteorológico... Hoy en Xalapa tendremos un día nublado"
    elif "hora" in frase or "tiempo" in frase:
        respuesta = "Consultando el reloj... Son las " + ahora.strftime("%H:%M") + " horas."
    else:
        respuesta = "Lo siento, no entiendo tu comando. ¿Podrías escribir otra palabra?"

    print(respuesta)
    print("Proceso finalizado. ¡Gracias por usar " + nombre_asistente + "!")

def main():
    clasificar_intencion()

if __name__ == "__main__":
    main()
    
