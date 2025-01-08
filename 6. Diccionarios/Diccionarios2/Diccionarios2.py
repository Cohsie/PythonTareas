
Listin = {}

def mostrarListin():
    if not Listin: #Si no hay listín...
        print("El listín está vacío")
    else:
        print("Listado de teléfonos: ")
        for nombre, telefono in Listin.items(): #Listin.items imprime las dos partes del diccionario. Poner los parénntesis alfinal para que no de error: no iterable
            print(f"{nombre}: {telefono}")

def mostrarAlfabetico():
    if not Listin:
        print("El listín está vacío")
    else:
        print("Listado de teléfonos por orden alfabético: ")
        for nombre, telefono in sorted(Listin):
            print(f"${nombre}: ${telefono}")

def anadir():
    nombre = input("Dime el nombre del contacto: ")
    telefono = int(input("Dime el número que quieres añadir: "))
    Listin[nombre] = telefono


def modificar():
    if not Listin:
        r = input("Desea añadir un nuevo número? Escríba si o no: ")
        if r.lower() == "si":
            anadir()
        else:
            print("Volviendo al menú")
    else:
        nombre = input("Dime el contacto que quieres buscar: ")
        if nombre in Listin:
            newTelefono = int(input("Dime el nuevo número de teléfono: "))
            Listin[nombre] = newTelefono
            print(f"Contacto {nombre} actualizado.")
        else:
            print("Contacto no encontrado.")

def buscaNumero():
    busca = int(input("Dime el número de teléfono que quieres buscar: "))
    for nombre, telefono in Listin.items():
        if telefono == busca:
            print(f"El número {telefono} pertenece a {nombre}")
            return
    print("Nombre no encontrado en el listín")        

def eliminaContacto():
    nombre = input("Dime el contacto que quieres elimianr: ")
    if nombre in Listin:
        del Listin[nombre]
        print(f"Contacto {nombre} eliminado")
    else:
        print("Contacto on encontrado.")
        
def borraListin():
    Listin.clear()

def menu():
    while True:
        print("a. Listado de teléfonos orden por defecto")
        print("b. Listado de teléfonos por orden alfabético")
        print("c. Añadir nuevo contacto")
        print("d. Modificar teléfono de un contacto")
        print("e. Buscar un número de teléfono")
        print("f. Eliminar un contacto")
        print("g. Borrar el listín telefónico")

        opcion = input("Escribe una opción: ").lower()

        match opcion:
            case "a":
                mostrarListin()
            case "b":
                mostrarAlfabetico()
            case "c":
                anadir()
            case "d":
                modificar()
            case "e":
                buscaNumero()
            case "f":
                eliminaContacto()
            case "g":
                borraListin()
            case default:
                print("Por favor elija una opción válida")


menu()
    