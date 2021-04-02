N = int(input())
X = []
X.append(input().split())
X = list(map(int, *X))
print("Menor valor: {0}".format(min(X)))
print("Posicao: {0}".format(X.index(min(X))))