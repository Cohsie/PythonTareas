#Escribe un programa que recoja un número y muestre un
#triángulo (como el ejercicio de kotlin)

counter = 0
num =int(input("Introduce un número "))
asterisco = "*"

while counter < num:
    print (asterisco)
    asterisco += "*"
    counter +=1