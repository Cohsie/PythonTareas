#4. Definir la función  
# rota : (int, List[A]) -> List[A]  
# tal que rota(n, xs) es la lista obtenida poniendo los n primeros  
# elementos de xs al final de la lista. Por ejemplo,  
# rota(1, [3, 2, 5, 7]) == [2, 5, 7, 3]  
# rota(2, [3, 2, 5, 7]) == [5, 7, 3, 2]  
# rota(3, [3, 2, 5, 7]) == [7, 3, 2, 5]  
from typing import List, TypeVar

A = TypeVar('A')#TypeVar es un tipo de variable que indica que se puede trabajar conn todo

def rota(n:int, lst: List[A]) -> List[A]:#Función de rotación a la que le pasamos una  lista para que ponga los primeros n elementos de la lista al final
    return lst[n:] + lst[:n]

lista = []
n = input("Introduce números para la lista. Espacio termina: ")

while n != " ":
    lista.append(int(n))
    n = (input("Escribe otro número(o espacio para terminar): "))

rotaciones = int(input("Dime el número de rotaciones: "))
print(f"Lista original {lista}")
print(f"Lista rotada {rotaciones} veces {rota(rotaciones, lista)}")



