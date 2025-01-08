hora = input("¿Qué hora es?")
hora = int(hora)

match hora:
    case hora if 7<= hora <12:
        print("Illo buenos días")
    case hora if 12<= hora <20:
        print("Buenas tardes illo")
    case _:
        print("Estoy illo durmiendo o esa hora no existe en nuestro sistema horario, buenas noches")