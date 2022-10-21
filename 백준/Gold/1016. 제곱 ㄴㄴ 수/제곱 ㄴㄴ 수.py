import math
N, M = list(map(int, input().split()))
checkList = [1] * (M-N+1)
for i in range(2, int(math.sqrt(M))+1):
    mul = N // (i ** 2)
    while mul * (i ** 2) <= M:
        if mul * (i ** 2) - N >=0 and mul * (i ** 2) - N <= M-N:
            checkList[mul * (i ** 2)- N] = 0
        mul +=1
print(sum(checkList))