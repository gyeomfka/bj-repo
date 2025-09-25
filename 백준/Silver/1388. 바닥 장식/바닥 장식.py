from collections import deque

n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(str, input())))

def bfs(arr):
    visited = [[False] * m for _ in range(n)]
    board_cnt = 0

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == '-' and not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                board_cnt += 1

                while q:
                    now_y, now_x = q.popleft()

                    if now_x == m - 1 or arr[now_y][now_x + 1] == '|':
                        break
                    else:
                        visited[now_y][now_x + 1] = True
                        q.append((now_y, now_x + 1))

            elif arr[i][j] == '|' and not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                board_cnt += 1

                while q:
                    now_y, now_x = q.popleft()

                    if now_y == n - 1 or arr[now_y + 1][now_x] == '-':
                        break
                    else:
                        visited[now_y + 1][now_x] = True
                        q.append((now_y + 1, now_x))
    return board_cnt

print(bfs(arr))