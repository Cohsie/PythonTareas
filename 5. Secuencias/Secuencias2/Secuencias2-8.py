# Ejercicio 8. Definir la función
# segmento : (int, int, list[A]) -> list[A]
# tal que segmento(m, n, xs) es la lista de los elementos de xs
# comprendidos entre las posiciones m y n. Por ejemplo,
# segmento(3, 4, [3, 4, 1, 2, 7, 9, 0]) == [1, 2]
# segmento(3, 5, [3, 4, 1, 2, 7, 9, 0]) == [1, 2, 7]
# segmento(5, 3, [3, 4, 1, 2, 7, 9, 0]) == []

from typing import List, TypeVar

A = TypeVar('A')

inicio = 0
final = 0

Lista = []

listado = input("Escribe un número. Espacio para terminar: ")

while listado != " ":
    Lista.append(int(listado))
    listado = input("Otro número: ")

def segmento (n: int, g:int, lst:list[A]) -> list[A]:
    lst[inicio:final]

inicio = input("Escribe el inicio")

final = input("Escribe el final")

print(f"Lista original: {Lista}")
print(f"Rango elegido: {segmento(inicio, final, Lista)}")