#4.Codifica un programa en python que nos permita guardar los nombres
#de los alumnos de una clase y las notas que han obtenido. Cada alumno
#puede tener distinta cantidad de notas.
#Guarda la información en un diccionario cuya claves serán los nombres
#de los alumnos y los valores serán listas con las notas de cada
#alumno.
#El programa pedirá el número de alumnos que vamos a introducir, pedirá
#su nombre e irá pidiendo sus notas hasta que introduzcamos un número
#negativo.
#Al final el programa nos mostrará la lista de alumnos y la nota media
#obtenida por cada uno de ellos.
#Nota: si se introduce el nombre de un alumno que ya existe el programa
#nos dará un error.



Diccionario = {}
numAlumnos = int(input("Dime cuantos alumnos vas a meter: "))


n = 0

while n < numAlumnos:
    nombres = input("Dime el nombre del alumno: ")

    notas = int(input("Dime la nota: ")) 

    if nombres in Diccionario:#Para comprobar si un alumno con el mismo nombre ya está metido. Si es el caso devuelve este print y continue
        print("Ese alumno ya está metido. Ingrese un nombre distinto")
        continue #Evita que se ejecute el resto de la iteracion del while para volver a empezar

    while notas >= 0:
        listaNotas = []#La creación de la lista debe ir dentro del while para que se resetee por cada alumno
        listaNotas.append(notas)
        notas = float(input("Dime otra nota: ")) 

    n += 1
    Diccionario[nombres] = listaNotas

print(Diccionario)

for i, n in Diccionario.items():
    print(i, sum(n)/len(n))
