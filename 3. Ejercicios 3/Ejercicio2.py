#Escribe un programa que recoja un número y calcule su factorial

num =int(input("dame un número"))


i = num

while i > 1:
    num = num * (i-1)   
    i -= 1

print(num)