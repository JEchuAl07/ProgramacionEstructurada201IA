def capturar_ventas(productos, dias):
    ventas = [[0] * 3 for _ in range(3)]
    for i in range(len(productos)):
        print(f"\n--- Registro para {productos[i]} ---")
        for j in range(len(dias)):
            ventas[i][j] = int(input(f"Ingrese ventas de {productos[i]} para el {dias[j]}: "))
    return ventas


def obtener_producto_estrella(productos, totales_por_producto):
    max_ventas = max(totales_por_producto)
    indice_ganador = totales_por_producto.index(max_ventas)
    producto_top = productos[indice_ganador]
    print(f"\nEL PRODUCTO MÁS VENDIDO ES: {producto_top} ({max_ventas} unidades)")
    print("="*45)


def mostrar_reporte(productos, ventas):
    print("\n" + "="*45)
    print(f"{'Producto':<12} | {'Lun':<5} {'Mar':<5} {'Mié':<5} | {'Total':<8}")
    print("-" * 45)

    total_general = 0
    totales_por_producto = []

    for i in range(len(productos)):
        suma_producto = sum(ventas[i])
        totales_por_producto.append(suma_producto)
        total_general += suma_producto
        print(f"{productos[i]:<12} | {ventas[i][0]:<5} {ventas[i][1]:<5} {ventas[i][2]:<5} | {suma_producto:<8}")

    print("-" * 45)
    promedio_ventas = total_general / (len(productos) * len(ventas[0]))
    print(f"VENTA TOTAL GENERAL: {total_general}")
    print(f"PROMEDIO DE VENTAS POR DÍA: {promedio_ventas:.2f}")

    obtener_producto_estrella(productos, totales_por_producto)


def main():
    lista_productos = ["Laptop", "Smartphone", "Tablet"]
    lista_dias = ["Lunes", "Martes", "Miércoles"]

    matriz_ventas = capturar_ventas(lista_productos, lista_dias)
    mostrar_reporte(lista_productos, matriz_ventas)


if __name__ == '__main__':
    main()