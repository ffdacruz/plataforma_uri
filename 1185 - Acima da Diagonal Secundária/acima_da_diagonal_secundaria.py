M = []
line_sum = 0.0

O = input()

for i in range(12):
    line_values = []
    for j in range(12):
        value = float(input())
        line_values.append(value)
    M.append(line_values)

columns = 12
count = 0

for l in range(11):
    columns -= 1
    for c in range(columns):
        line_sum += M[l][c]
        count += 1

if O == 'S':      
    print('{0:.1f}'.format(line_sum))      
elif O == 'M':
    print('{0:.1f}'.format(line_sum / (((12 * 12) - 12) / 2))) #66.0