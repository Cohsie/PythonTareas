p1 = input("Escribe una palabra: ")
p2 = input("Escribe otra palabra: ")

if p1 == p2[::-1]:
    print("Una es palíndromo de la otra")
else:
    print("No son palíndromas")