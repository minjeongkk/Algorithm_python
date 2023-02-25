# 거스름돈

N = int(input())
result = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    result += N//coin
    N = N %coin

print(result)