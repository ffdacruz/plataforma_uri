numeros = []
quantidade_positivos = 0
soma_positivos = 0
media = 0.0

for numero in range(0, 6):
    numeros.append(float(input()))

for x in numeros:
    if x >= 0:
        quantidade_positivos += 1 
        soma_positivos += x

media = soma_positivos / quantidade_positivos

print('{0} valores positivos'.format(quantidade_positivos))
print('{0:.1f}'.format(media))