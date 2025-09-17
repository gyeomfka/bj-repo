import sys
from collections import deque

input = sys.stdin.readline  # input() 대체


# 큐 생성
queue = deque()
cnt = int(input().strip())

results = []

for _ in range(cnt):
    command = input().split()

    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        results.append(queue.popleft() if queue else -1)
    elif command[0] == 'size':
        results.append(len(queue))
    elif command[0] == 'empty':
        results.append(0 if queue else 1)
    elif command[0] == 'front':
        results.append(queue[0] if queue else -1)
    elif command[0] == 'back':
        results.append(queue[-1] if queue else -1)

# 한 번에 출력
sys.stdout.write("\n".join(map(str, results)))