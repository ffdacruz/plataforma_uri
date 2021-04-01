M = []
line_sum = 0.0

O = input()

for i in range(12):
    line_values = []
    for j in range(12):
        value = float(input())
        line_values.append(value)
    M.append(line_values)

for l in range(12):
    for c in range(12):
        if c < l:
            line_sum += M[l][c]

if O == 'S':      
    print('{0:.1f}'.format(line_sum))      
elif O == 'M':
    print('{0:.1f}'.format(line_sum / (((12 * 12) - 12) / 2))) #66.0