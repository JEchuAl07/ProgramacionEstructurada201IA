"""
Semanas trabajadas para meta financiera
"""

def semanas_trabajadas():
    meta = 2500
    total_acumulado = 0
    semanas = 0
    while total_acumulado < meta:
        salario_semanal = int(input("¿Cuál es el salario en esta semana? "))
        total_acumulado += salario_semanal
        semanas += 1
    return semanas

def main():
    resultado = semanas_trabajadas()
    print("Semanas trabajadas para alcanzar la meta:", resultado)

if __name__ == "__main__":
    main()