#Ejercicio 2

numero1 = float(input("Inserte el primer número: "))
numero2 = float(input("Inserte el segndo número: "))
operador = input("Escriba la operación que desee realizar: ")

def calculo(operador, numero1, numero2):
    return{
        'suma': lambda: numero1 + numero2,
        'resta': lambda: numero1 - numero2,
        'multiplicación': lambda: numero1 * numero2,
        'división': lambda: numero1 / numero2
    }.get(operador, lambda: None)
