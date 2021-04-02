# 1185 - Acima da Diagonal Secundária

Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão acima da diagonal secundária da matriz, conforme ilustrado abaixo (área verde).

### Entrada
A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.

### Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.

### Resposta

```python
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
```