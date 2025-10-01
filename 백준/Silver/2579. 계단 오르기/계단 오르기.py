"""
계단문제
"""

def solve():
    cnt = int(input())
    arr = [0] + [int(input().strip()) for _ in range(cnt)]

    if cnt == 0:
        print(0)
        return

    if cnt == 1:
        print(arr[1])
        return

    if cnt == 2:
        print(arr[1] + arr[2])
        return

    dp = [0] * (cnt + 1)
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]

    for i in range(3, cnt + 1):
        dp[i] = max(dp[i - 2] + arr[i],
                    dp[i - 3] + arr[i - 1] + arr[i])

    print(dp[cnt])

solve()
