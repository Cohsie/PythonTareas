# Programa para varios usuarios
usuarios = []

while True:
    # Crear un diccionario para cada usuario
    usuario = {}
    usuario["nombre"] = input("Ingrese su nombre: ")
    usuario["edad"] = input("Ingrese su edad: ")
    usuario["direccion"] = input("Ingrese su dirección: ")
    usuario["telefono"] = input("Ingrese su número de teléfono: ")
    
    # Añadir el usuario a la lista de usuarios
    usuarios.append(usuario)
    
    # Preguntar si desea añadir otro usuario
    continuar = input("¿Desea añadir otro usuario? (sí/no): ").strip().lower()
    if continuar != "sí":
        break

# Mostrar la información de todos los usuarios
for usuario in usuarios:
    print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su número de teléfono es {usuario['telefono']}.")
