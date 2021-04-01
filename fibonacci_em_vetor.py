T = int(input())

for i in range(T):

    N = int(input())

    if 0 <= N and N <= 60:

        fibonacci_numbers = [0, 1]

        if N > 1:
            for j in range(2, N + 1):
                fibonacci_numbers.append(fibonacci_numbers[j - 2] + fibonacci_numbers[j - 1])
            print('Fib({0}) = {1}'.format(N,fibonacci_numbers[N]))

        if N <= 1:
            print('Fib({0}) = {1}'.format(N,fibonacci_numbers[N]))