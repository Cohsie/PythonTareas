anio = input("Escribe el año que quieras saber")

anio = int(anio)

if anio % 4 == 0 and (anio % 100 != 0 and anio % 400 == 0):
        print("El año es bisiesto")
else:
        print("El año no es bisiesto")