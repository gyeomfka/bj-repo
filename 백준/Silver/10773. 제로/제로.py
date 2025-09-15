"""
잘못된 수를 부를때 0을 외친다.
"""
cnt = int(input())
stack = []

for i in range(cnt):
    value = int(input())
    if value == 0:
        stack.pop()
    else:
        stack.append(value)

print(sum(stack))