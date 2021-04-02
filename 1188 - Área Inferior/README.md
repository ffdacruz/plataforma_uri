# 1188 - Área Inferior

Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão na área inferior da matriz, conforme ilustrado abaixo (área verde).

### Entrada
A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante de dupla precisão (double) que compõem a matriz.

### Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.

### Resposta

```python
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
```