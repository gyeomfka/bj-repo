n = int(input())
arr = [0] * (n + 1)

def solve(z):
    for i in range(2, z + 1):
        arr[i] = arr[i - 1] + 1

        if i%2 == 0:
            arr[i] = min(arr[i], arr[i//2] + 1)

        if i%3 == 0:
            arr[i] = min(arr[i], arr[i//3] + 1)

    return arr[z]

print(solve(n))