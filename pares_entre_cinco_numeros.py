quantidade_pares = 0

for numero in range(0, 5):
    numero = int(input())    
    if numero % 2 == 0:
        quantidade_pares += 1

print('{0} valores pares'.format(quantidade_pares))