# Analizador de texto con IA

def normalizar_mensaje():
    texto = input("Ingrese su mensaje: ").lower()
    return texto

def detectar_intencion(texto):
    if "encender" in texto or "activar" in texto or "reproducir" in texto:
        return "COMANDO DE ACCIÓN"
    elif "ayuda" in texto or "error" in texto or "fallo" in texto:
        return "REPORTE DE SOPORTE"
    else:
        return "CONSULTA GENERAL"
    
def main():
    texto_normalizado = normalizar_mensaje()
    intencion = detectar_intencion(texto_normalizado)
    longitud = len(texto_normalizado)
    
    print("\n--- Resultados del Análisis ---")
    print("Texto normalizado:", texto_normalizado)
    print(f"Categoría detectada: {intencion}")
    print(f"Longitud del mensaje: {longitud} caracteres")

if __name__ == "__main__":
    main()