mes = input("Escribe un mes por número")

match mes:
    case 1:
        print("Tiene 31 días")
    case 2:
        print("Tiene 28 o 29 días")
    case 3:
        print("Tiene 31 días")
    case 4:
        print("Tiene 30 días")
    case 5:
        print("Tiene 31 días")
    case 6:
        print("Tiene 30 días")
    case 7:
        print("Tiene 31 días")
    case 8:
        print("Tiene 31 días")
    case 9: 
        print("Tiene 30 días")
    case 10:
        print("Tiene 31 días")
    case 11:
        print("Tiene  30 días")
    case 12:
        print("Tiene 31 días")
    case _:
        print("Ese año no existe")