from collections import defaultdict

n = int(input())
dic = defaultdict(int)
for i in range(n):
    x, y = list(map(int, input().split()))
    if x in dic:
        dic[x] = min(dic[x], y)
    else:
        dic[x] = y

answer = 0
for i in dic.values():
    answer += i
print(answer)