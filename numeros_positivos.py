positivos = 0
numeros = []

for i in range(0,6):
    numeros.append(float(input()))

for numero in numeros:
    if numero >= 0:
        positivos += 1

print('{0} valores positivos'.format(positivos))