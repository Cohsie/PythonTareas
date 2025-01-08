#5. Escribe un programa que calcule el precio de entrada a un museo a partir de la edad del visitante, teniendo en cuenta que:
#a. Menores de 5 años entran gratis.
#b. Niños entre 5 años y 18 (sin llegar a los 18) pagan 3€.
#c. Mayores de edad hasta los 65 (sin llegar a los 65) pagan 6€.
#d. Jubilados entran gratis.

edad = input("Dime tu edad: ")

edad = int(edad)

match edad:
    case edad if edad <5:
        print("Entras gratis chiquitín")
    case edad if 5>= edad <18:
        print("Te toca pagar 3€ crack")
    case edad if 18>= edad <65:
        print("Eres adulto, págame 6€")
    case edad if 65>= edad:
        print("Usted participó en la guerra y defendió el país, pase gratis por favor")