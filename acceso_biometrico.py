# acceso_biometrico.py

def evaluar_acceso(nombre, id_empleado, iris_match, facial_match):
    """
    Procesa las firmas biométricas y determina el nivel de acceso.
    Retorna el mensaje de diagnóstico correspondiente.
    """
    # 1. INTRUSO (Alarma) - Se evalúa primero por seguridad
    if id_empleado <= 0:
        return "¡ALERTA DE SEGURIDAD! ID inválido detectado. Bloqueando accesos y notificando a la policía."
    
    # 2. ACCESOS CONTRALADOS (Ambos escaneos correctos)
    elif iris_match == "si" and facial_match == "si":
        if id_empleado < 100:
            # ACCESO TOTAL (Senior)
            mensaje = f"Bienvenido, Ingeniero {nombre}. Acceso nivel SENIOR concedido a todas las áreas."
        else:
            # ACCESO RESTRINGIDO (Junior)
            mensaje = f"Bienvenido, Ingeniero {nombre}. Accesso nivel JUNIOR concedido. Áreas de servidores restringidas."
        
        # Reto Adicional: Agregar la generación de log al mensaje
        mensaje += f"\nGenerando log de entrada para el usuario: {id_empleado}..."
        return mensaje
    
    # 3. PROTOCOLO DE FALLO BIOMÉTRICO (ID válido, pero alguna biometría falló)
    else:
        return "Error Biométrico: Identidad no verificada al 100%. Por favor, contacte a seguridad."


def main():
    print("--- SISTEMA DE CONTROL BIOMÉTRICO ---")
    
    # Captura y limpieza de datos
    nombre = input("Nombre del Ingeniero: ")
    
    try:
        id_empleado = int(input("ID de Empleado: "))
    except ValueError:
        print("\n> Diagnóstico: Error: El ID debe ser un número entero.")
        return

    # Usamos .lower() para estandarizar las respuestas
    iris_match = input("¿El escaneo de Iris coincide? (si/no): ").lower()
    facial_match = input("¿El reconocimiento facial es > 95%? (si/no): ").lower()
    
    # Procesamiento
    diagnostico = evaluar_acceso(nombre, id_empleado, iris_match, facial_match)
    
    # Salida
    print(f"\n> Diagnóstico: {diagnostico}")


if __name__ == "__main__":
    main()