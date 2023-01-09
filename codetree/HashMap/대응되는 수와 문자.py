n, m = list(map(int, input().split()))

dic = dict()
dic2 = dict()
for i in range(n):
    data = input()
    dic[data] = i+1
    dic[f"{i+1}"] = data

for _ in range(m):
    data = input()
    if data in dic:
        print(dic[data])
    else:
        print(dic2[data])
