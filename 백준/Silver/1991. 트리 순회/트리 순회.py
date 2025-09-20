import sys

input = sys.stdin.readline

# 노드 개수
N = int(input().strip())

# 트리 저장용 딕셔너리
tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

def pre_order(node: str):
    if node == '.':
        return
    print(node, end='')
    pre_order(tree[node][0])
    pre_order(tree[node][1])

def in_order(node: str):
    if node == '.':
        return
    in_order(tree[node][0])
    print(node, end='')
    in_order(tree[node][1])

def post_order(node: str):
    if node == '.':
        return
    post_order(tree[node][0])
    post_order(tree[node][1])
    print(node, end='')

pre_order('A')
print("")
in_order('A')
print("")
post_order('A')