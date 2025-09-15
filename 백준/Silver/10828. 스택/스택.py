cnt = int(input())

stack = []

for i in range(cnt):
    input_value = input().split()

    if len(input_value) == 2:
        order, value = input_value
        if order == 'push':
            stack.append(value)
    elif len(input_value) == 1:
        order = input_value[0]
        b = None

        if order == 'pop':
            if len(stack) > 0:
                print(stack.pop())
            else:
                print(-1)
        elif order == 'size':
            print(len(stack))
        elif order == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif order == 'top':
            if len(stack) > 0:
                print(stack[len(stack) - 1])
            else:
                print(-1)
    else:
        a = b = None



