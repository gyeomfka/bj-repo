
size = int(input())
arr = [list(map(int, input().split())) for _ in range(size)]

def is_uniform(arr, r1, r2, c1, c2):
    value = arr[r1][c1]
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            if value != arr[r][c]:
                return False, None
    return True, value

# arr, 0, 7, 1
# param arr, rows범위1 rows범위2 cols범위1 cols범위2 비교할 대상
def validate(arr, r1, r2, c1, c2):
    result, value = is_uniform(arr, r1, r2, c1, c2)
    if result:
        if value == 0:
            return (1,0)
        else:
            return (0,1)

    r_mid = (r1 + r2) // 2
    c_mid = (c1 + c2) // 2

    w1, b1 = validate(arr, r1, r_mid, c1, c_mid) # 1사분면
    w2, b2 = validate(arr, r1, r_mid, c_mid + 1, c2) # 2사분면
    w3, b3 = validate(arr, r_mid + 1, r2, c1, c_mid) # 3사분면
    w4, b4 = validate(arr, r_mid + 1, r2, c_mid +1 , c2) # 4사분면
    return (w1 + w2 + w3 + w4, b1 + b2 + b3 + b4)

white_cnt, blue_cnt = validate(arr, 0, size-1, 0, size - 1)

print(white_cnt)
print(blue_cnt)