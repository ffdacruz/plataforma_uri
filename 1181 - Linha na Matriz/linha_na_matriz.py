M = []
line_sum = 0.0

L = int(input())
T = input()

for i in range(12):
    line_values = []
    for j in range(12):
        value = float(input())
        line_values.append(value)
    M.append(line_values)

for l in range(12):
    for c in range(12):
        if l == L:
            line_sum += M[l][c]

if T == 'S':      
    print('{0:.1f}'.format(line_sum))      
elif T == 'M':
    print('{0:.1f}'.format(line_sum/12))