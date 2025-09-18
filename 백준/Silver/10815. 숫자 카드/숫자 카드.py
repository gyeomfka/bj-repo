cnt = int(input())
given_arr = list(map(int, input().split()))
given_arr.sort() # -10, 2, 3, 6, 10 

target_cnt = int(input())
target_arr = list(map(int, input().split())) # 10, 9, -5, 2, 3, 4, 5, -10

def binary_search(given_arr, start, end, target_value):
    if start > end:
        return 0

    mid = (start + end) // 2

    if given_arr[mid] == target_value:
        return 1
    elif given_arr[mid] > target_value:
        return binary_search(given_arr, start, mid - 1, target_value)
    else:
        return binary_search(given_arr, mid + 1, end, target_value)

for i in target_arr:
    print(binary_search(given_arr, 0, len(given_arr) - 1, i), end=' ')