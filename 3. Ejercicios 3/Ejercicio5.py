#Escribe un programa que recoja un número por teclado y muestre los primeros
#cuadrados hasta llegar al número introducido. Por ejemplo, si se ha introducido
#el valor 5, se debe mostrar:

num = int(input("Dame un número"))

i = num
k = 1

while i > 0:
    print(k**2)
    k += 1
    i -= 1