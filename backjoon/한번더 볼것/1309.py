import math
# 2 이상 제곱수로 나누어 떨어지지 않을 때 제곱 ㄴㄴ 수
N, M = list(map(int, input().split()))
# 배열을 만들면 무조건 터진다.
# 단순히 계산으로 끝내야 할듯
checkList = [1] * (M-N+1)
for i in range(2, int(math.sqrt(M))+1):
    mul = N // (i ** 2)
    while mul * (i ** 2) <= M:
        if mul * (i ** 2) - N >=0 and mul * (i ** 2) - N <= M-N:
            checkList[mul * (i ** 2)- N] = 0
        mul +=1
print(sum(checkList))

# import math
# min, max = map(int, input().split())
# validate = [1 for i in range(max-min+1)]
# cnt=0
# i=2
# while i**2 <= max:
#     mul = min // i**2
#     while mul * (i**2) <= max:
#         if mul * (i**2) - min >= 0 and mul * (i**2) - min <= max-min:
#             validate[mul * (i**2) - min] = 0
#         mul +=1
#     i +=1
#
# print(sum(validate))