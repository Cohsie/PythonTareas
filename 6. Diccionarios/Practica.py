vacio = {}#Ejemplo de creación de un diccionario

precios = {
    "Pera": 1.60,
    "Ciruela": 1.24,
    "Manzana": 1.75
}

#También se puede crear la función dict()

vacio2 = dict()

precios2 = dict(
    Pera=1.60,
    Ciruela=1.24,
    Manzana=1.75
)

#Añadir o modificar elementos

precios["Sandía"] = 0.99

#Comprobar si una clave existe en el diccionario

#if "Pera" in precios:

print(precios)

for c in precios.keys():
    print(c)

for c in precios.items():
    print(c)