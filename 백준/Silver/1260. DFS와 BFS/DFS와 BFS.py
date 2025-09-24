from collections import deque

class Graph:
    def __init__(self, n: int):
        self.n = n
        self.adj_list = [[] for _ in range(n + 1)]

    def add_edge(self, u: int, v: int):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def dfs(self, n):
        visited = [False] * (self.n + 1 )
        stack = [n]

        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                print(node, end = " ")
                self.adj_list[node].sort()
                for nxt in reversed(self.adj_list[node]):
                    if not visited[nxt]:
                        stack.append(nxt)

    def bfs(self, n):
        visited = [False] * (self.n + 1)
        queue = deque([n])
        visited[n] = True

        while queue:
            node = queue.popleft()
            print(node, end = " ")
            self.adj_list[node].sort()
            for next in self.adj_list[node]:
                if not visited[next]:
                    visited[next] = True
                    queue.append(next)


graph_cnt, cnt, start = map(int, input().split())
graph = Graph(graph_cnt)
for _ in range(cnt):
    u, v = map(int, input().split())
    graph.add_edge(u, v)


graph.dfs(start)
print("")
graph.bfs(start)