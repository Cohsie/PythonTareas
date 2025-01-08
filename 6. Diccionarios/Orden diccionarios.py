diccionario = {"abc": "1234", "d": "56", "efgh": "789", "i": "0"}

# 1. Ordenar por clave ascendente (por defecto)
print("Ordenar por clave ascendente:")
for clave, valor in sorted(diccionario.items()):
    print(clave, valor)

# 2. Ordenar por clave descendente
print("\nOrdenar por clave descendente:")
for clave, valor in sorted(diccionario.items(), key=lambda x: x[0], reverse=True):
    print(clave, valor)

# 3. Ordenar por longitud de la clave (ascendente)
print("\nOrdenar por longitud de clave ascendente:")
for clave, valor in sorted(diccionario.items(), key=lambda x: len(x[0])):
    print(clave, valor)

# 4. Ordenar por longitud de la clave (descendente)
print("\nOrdenar por longitud de clave descendente:")
for clave, valor in sorted(diccionario.items(), key=lambda x: len(x[0]), reverse=True):
    print(clave, valor)

# 5. Ordenar por longitud del valor (ascendente)
print("\nOrdenar por longitud de valor ascendente:")
for clave, valor in sorted(diccionario.items(), key=lambda x: len(x[1])):
    print(clave, valor)

# 6. Ordenar por longitud del valor (descendente)
print("\nOrdenar por longitud de valor descendente:")
for clave, valor in sorted(diccionario.items(), key=lambda x: len(x[1]), reverse=True):
    print(clave, valor)
