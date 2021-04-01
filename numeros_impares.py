X = int(input())

if 1 <= X and X <= 1000:
    for impar in range(1, X+1):
        if impar % 2 != 0:
            print(impar)