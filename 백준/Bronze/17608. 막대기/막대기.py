import sys

cnt = int(sys.stdin.readline())
stack = [int(sys.stdin.readline()) for _ in range(cnt)]
answer = 0
right = stack.pop()
now_right_max = right

# for i in reversed(range(len(stack))):
while len(stack) > 0:
    now_pop_value = stack.pop()

    if now_pop_value > now_right_max:
        answer += 1
        now_right_max = now_pop_value

print(answer + 1)