price = int(input())

dp = [0] * (price + 1)

def solve(price):
    if price == 0 or price == 1 or price == 3:
        return -1
    else:
        if price%5 == 0:
            return price//5
        elif price%5 == 1:
            return price//5 + 2
        elif price%5 == 2:
            return price//5 + 1
        elif price%5 == 3:
            return price//5 + 3
        elif price%5 == 4:
            return price//5 + 2

print(solve(price))