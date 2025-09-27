def fibo(n, memo):
    if n == 0 or n == 1:
        return n

    if not memo.get(n):
        memo[n] = fibo(n-2, memo) + fibo(n-1, memo)

    return memo[n]

memo = {}
print(fibo(int(input()), memo))

