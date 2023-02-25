# 시각

n = int(input())
cnt = 0
for i in range(n+1):
    # 시각에 3이 들어가면 그 시간만큼 다 더함
    if i==3 or i==13 or i==23:
        cnt += 60*60
    # 시각에 3이 들어가지 않으면 전체-3이 안들어가는 시각을 빼서 더함
    else:
        cnt +=(60*60-45*45)
print(cnt)

# n = int(input())
# cnt = 0
# for i in range(n+1):
#     for j in range(60):
#         for k in range(60):
#             # 매 시각에 '3'이 포함되어 있다면 카운트 증가
#             if '3' in str(i)+str(j)+str(k):
#                 cnt +=1
# print(cnt)