cnt = int(input())

arr = []
def solve(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n >= 4:
        return solve(n-1) + solve(n-2) + solve(n-3)

for _ in range(cnt):
    print(solve(int(input())))