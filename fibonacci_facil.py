N = int(input())
numeros = []

if 0 < N and N < 46:
    for x in range(0, N):
        if x == 0 or x == 1:
            numeros.append(x)
        else:
            numeros.append(numeros[x - 1] + numeros[x - 2])

print(*numeros, sep=' ')
