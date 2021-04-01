M = []
values_sum = 0.0

O = input()

for i in range(12):
    line_values = []
    for j in range(12):
        value = float(input())
        line_values.append(value)
    M.append(line_values)

inf = 5
sup = 7
count = 0

for l in range(7, 12):
    for c in range(inf, sup):
        values_sum += M[l][c]
        count += 1
    inf -= 1
    sup += 1 

if O == 'S':      
    print('{0:.1f}'.format(values_sum))      
elif O == 'M':
    print('{0:.1f}'.format(values_sum / count))