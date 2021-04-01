N = []
N.append(float(input()))

print('N[0] = {0:.4f}'.format(N[0]))

for i in range(1, 100):
    N.append(N[i-1]/2)
    print('N[{0}] = {1:.4f}'.format(i, N[i]))