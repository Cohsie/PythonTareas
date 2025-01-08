print ("Escribe un número por teclado")
num = input()

match num:
    case 1:
        print ("Estamos a lunes")
    case 2:
        print ("Estamos a martes")
    case 3:
        print ("Estamos a miercoles")
    case 4:
        print ("Estamos a jueves")
    case 5:
        print ("Estamos a viernes")
    case 6:
        print ("Estamos a sábado")
    case 7:
        print ("Estamos a domingo")
    case _:
        print ("Error, eso no vale")