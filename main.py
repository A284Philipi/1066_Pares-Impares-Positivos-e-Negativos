cont = int(0)
pares = int(0)
impares = int(0)
negativos = int(0)
positivos = int(0)
while cont < 5:
    numero = int(input())
    if (numero%2) == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    if numero > 0:
        positivos = positivos + 1
    elif  numero < 0:
        negativos = negativos + 1
    cont = cont + 1
print("{} valor(es) par(es)".format(pares))
print("{} valor(es) impar(es)".format(impares))
print("{} valor(es) positivo(s)".format(positivos))
print("{} valor(es) negativo(s)".format(negativos))