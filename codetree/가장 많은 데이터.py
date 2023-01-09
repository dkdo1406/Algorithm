from collections import defaultdict
n = int(input())

dic = defaultdict(int)

for _ in range(n):
    dic[input()] += 1
print(max(dic.values()))