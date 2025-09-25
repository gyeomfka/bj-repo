from collections import deque

input_cnt = int(input())
arr = []

for _ in range(input_cnt):
    arr.append(list(map(int, input())))

    # 상, 하, 좌, 우
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]
answer = []

def bsf(arr):
    visited = [[False] * len(arr) for _ in range(len(arr[0]))]
    cnt = 0

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            house_cnt = 0
            if arr[i][j] == 1 and not visited[i][j]:
                house_cnt += 1
                visited[i][j] = True
                q = deque()
                q.append((i, j))

                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nh = x + dh[d]
                        nw = y + dw[d]

                        if 0 <= nh < len(arr) and 0 <= nw < len(arr[0]):
                            if arr[nh][nw] == 1 and not visited[nh][nw]:
                                visited[nh][nw] = True
                                house_cnt += 1
                                q.append([nh, nw])
                cnt += 1                
                answer.append((cnt, house_cnt))
                    
                
bsf(arr)

answer = sorted(answer, key=lambda x: x[1])

print(len(answer))
for i in range(len(answer)):
    print(answer[i][1])