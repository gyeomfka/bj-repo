import sys
from collections import deque

input = sys.stdin.readline  # input() 대체
cnt = int(input().strip())

queue = deque()

for i in range(cnt):
    queue.append(i+1)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])