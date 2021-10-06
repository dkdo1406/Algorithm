# # 재귀함수
# def INF(n):
#     if n<=1:
#         return 1
#     else:
#         return n * INF(n-1)
# print(INF(5))

# 반복함수
n = 5
result = 1
for i in range(n,0,-1):
    print(i)
    result *= i
print(result)