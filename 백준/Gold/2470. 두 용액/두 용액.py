
def find_closet_pair(arr):
    arr.sort()
    left, right = 0, len(arr) - 1

    best_sum = float("inf")
    best_left, best_right = arr[left], arr[right]

    while left < right:
        current_sum = arr[left] + arr[right]

        if abs(current_sum) < abs(best_sum):
            best_sum = current_sum
            best_left, best_right = arr[left], arr[right]

        if current_sum < 0:
            left += 1
        else:
            right -= 1

    print(best_left, best_right)

cnt = int(input())
arr = list(map(int, input().split()))
find_closet_pair(arr)
