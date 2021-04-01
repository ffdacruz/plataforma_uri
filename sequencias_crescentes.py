x = int(input())
numeros = []

while x != 0:
    for numero in range(1, x + 1):
        numeros.append(numero)
        
    print(*numeros, sep=' ')
    numeros.clear()
    x = int(input())