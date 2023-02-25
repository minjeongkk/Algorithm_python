# 큰 수의 법칙

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)

result = 0

# cnt = m//k
# for i in range(cnt+1):
#     if i==cnt:
#         if i%2==0:
#             result += nums[0]*(m%k)
#         else:
#             result += nums[1]*(m%k)
#         break

#     if i%2==0:
#         result += nums[0]*k
#     else : 
#         result += nums[1]*k
# print(result)

first = nums[0]
second = nums[1]

first_count = k*(m//(k+1)) + m%(k+1)
second_count = m-first_count

result= first*first_count+second*second_count
print(result)