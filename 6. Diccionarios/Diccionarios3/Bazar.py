ventas = {
    "A": {1: 5, 2: 3, 3: 6, 4: 8, 5: 1},
    "B": {1: 3, 2: 7, 3: 2, 4: 0, 5: 4},
    "C": {1: 6, 2: 4, 3: 3, 4: 5, 5: 2},
    "D": {1: 0, 2: 2, 3: 1, 4: 3, 5: 0}
}

totales = {}

for producto in ventas:
    ventasProducto = ventas[producto]  # Acceso a los valores de cada producto
    print(f"Producto {producto}:")
    print(ventasProducto)  # Imprimir el día y la cantidad vendida

    # 1. Ventas mensuales de cada producto
    totalVentas = sum(ventasProducto.values())  # Sumar todas las ventas individuales
    print(f"Venta total del producto {producto}: {totalVentas}")

    totales[producto] = totalVentas  # Agregar las ventas totales al diccionario

# 2. Producto más vendido y menos vendido del mes
max_ventas = max(totales.values())
min_ventas = min(totales.values())

producto_max = max(totales, key=totales.get)
producto_min = min(totales, key=totales.get)

print(f"El producto más vendido es {producto_max} con {max_ventas} unidades")
print(f"El producto menos vendido es {producto_min} con {min_ventas} unidades")

# 3. Mostrar las ventas diarias del producto más vendido
print(f"Las ventas del producto más vendido ({producto_max}) son: {ventas[producto_max]}")

# 4. Encontrar el día con la mayor venta para cada producto
for producto, ventasProducto in ventas.items():
    diaBueno = max(ventasProducto, key=ventasProducto.get)  # Día con mayor venta
    print(f"Día con más ventas del producto {producto}: {diaBueno} (Ventas: {ventasProducto[diaBueno]})")
