#숫자 카드 게임

n, m = map(int, input().split())
mins = []
for i in range(n):
    nums = list(map(int,input().split()))
    mins.append(min(nums))
print(max(mins))