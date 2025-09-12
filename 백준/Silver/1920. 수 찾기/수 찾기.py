"""
[문제]
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
"""
# 문제 입력
n = int(input())
target_arr = list(map(int, input().split()))

m = int(input())
given_arr = list(map(int, input().split()))
# 문제 입력 끝

target_arr.sort()

def binary_search(arr, target_num, start_index, end_index):
    if start_index > end_index:
        return 0

    mid_index = (start_index + end_index) // 2

    if target_num == arr[mid_index]:
        return 1
    elif target_num > arr[mid_index]:
        return binary_search(arr, target_num, mid_index + 1, end_index)
    else:
        return binary_search(arr, target_num, start_index, mid_index - 1)

for i in given_arr:
    print(binary_search(target_arr, i, 0, len(target_arr) - 1))