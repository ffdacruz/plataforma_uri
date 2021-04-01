M, N = input().split()
M, N = int(M), int(N)
numeros = []
soma = 0

while M > 0 and N > 0:
    if N > M:
        for x in range(M, N + 1):
            soma += x
            numeros.append(x)
    else:
        for x in range(N, M + 1):
            soma += x
            numeros.append(x)
    
    print(*numeros, sep=' ', end=' Sum={}\n'.format(soma))
    soma = 0
    numeros.clear()
    M, N = input().split()
    M, N = int(M), int(N)
