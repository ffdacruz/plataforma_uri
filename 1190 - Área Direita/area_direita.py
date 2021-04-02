M = []
values_sum = 0.0

O = input()

for i in range(12):
    line_values = []
    for j in range(12):
        value = float(input())
        line_values.append(value)
    M.append(line_values)

col = 11
count = 0

for l in range(1, 11):
    for c in range(col, 12):
        values_sum += M[l][c]
        count += 1
    if l < 5:
        col -= 1
    elif l > 5:
        col += 1

if O == 'S':      
    print('{0:.1f}'.format(values_sum))      
elif O == 'M':
    print('{0:.1f}'.format(values_sum / count))