import sys
from collections import deque
"""
요세푸스 문제
1 ~ N : N명의 사람이 원을 이루며 앉아있다
양의 정수 K 순서대로 K번째 사람을 제거한다
1 2 3 4 5 6 7

3 6 2 7 5 1 4
"""
queue = deque()

input = sys.stdin.readline  # input() 대체
cnt, k = list(map(int, input().split()))

arr = []
for i in range(cnt):
    arr.append(i + 1)

def get_person(s, k, cnt):
    index = s + k - 1

    while index > len(arr) - 1:
        index = index - len(arr)
    return index, arr[index]

s = 0
while len(arr) > 0:
    s, person = get_person(s, k, cnt)
    arr.remove(person)
    queue.append(person)

print("<" + ", ".join(map(str, queue)) + ">")
