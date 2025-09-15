"""

"""
cnt = int(input())
strings = []
for _ in range(cnt):
    s = input()   # 개행 기준으로 문자열 입력
    strings.append(s)

def validation(str):
    stack = []
    for x in str:
        if x == '(':
            stack.append(x)
        else:
            if len(stack) == 0:
                return "NO"
            else:
                stack.pop()

    if len(stack) == 0:
        return "YES"
    else:
        return "NO"

for string in strings:
    print(validation(string))

# print(validation(str))
# for i in range(cnt):
#     print(validation(input()))