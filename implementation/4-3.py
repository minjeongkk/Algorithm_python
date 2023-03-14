# 왕실의 나이트

loc = input()
x = ord(loc[0])-ord('a')+1
y = loc[1]

# 나이트가 이동할 수 있는 8가지 방향
moves = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

# 8가지 방향에 대해 이동가능한지 확인
count = 0
for move in moves:
    # 이동하는 위치
    dx = int(x) + move[0]
    dy = int(y) + move[1]
    # 이동이 가능하다면 카운트 증가
    if dx>0 or dy>0 or dx<=8 or dy<=8:
        count += 1
print(count)