
def cuentaVocales(texto):
    counter = 0
    for letra in texto:
        if letra in 'aeiou':
            counter +=1
    print (counter)


texto = input("Escribe una palabra: ")
cuentaVocales(texto)
