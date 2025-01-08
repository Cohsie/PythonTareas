diccionario = {}

nombre = input("Dime tu nombre\n")
diccionario["nombre"] = nombre

edad = int(input("Dime tu edad\n"))
diccionario["edad"] = edad

direccion = input("Donde vives?\n")
diccionario["direccion"] = direccion

telefono = int(input("Dime tu teléfono\n"))
diccionario["telefono"] = telefono


print(diccionario.get("nombre") + " tiene " + str(diccionario.get("edad")) + " años, vive en " 
      + diccionario.get("direccion")   
      + " y su numero de telefono es " + str(diccionario.get("telefono")))