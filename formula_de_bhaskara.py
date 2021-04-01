from math import sqrt

A, B, C = input().split()
A, B, C = float(A), float(B), float(C)
D = ( B *B ) - 4 * A * C

if D >= 0 and A != 0:
    print('R1 = {0:.5f}'.format(((B * -1) + sqrt(D)) / (2 * A)))
    print('R2 = {0:.5f}'.format(((B * -1) - sqrt(D)) / (2 * A)))
else:
    print('Impossivel calcular')