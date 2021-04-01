S = 0

for numero in range(1, 101):
    S = float( S + (1 / float(numero)))

print('{0:.2f}'.format(S))