nota = input("Introduce la calificación numérica de Pepito: ")

nota = float(nota)

match nota:
    case nota if nota <= 4:
        print("Estás suspenso, haber estudiao")
    case nota if 5 >= nota <6:
        print("Suficiente pero veo poco esfuerzo aquí")
    case nota if 6>= nota <7:
        print("Ta bien")
    case nota if 7>= nota <9:
        print("Notable")
    case nota if 9>= nota <10:
        print("Sobresaliente")
    case nota if nota == 10:
        print("Matrícula de honor")
    case _:
        print("Valor no válido")