from collections import defaultdict
dic = defaultdict(int)
for _ in range(10):
    dic[int(input()) % 42] += 1
print(len(dic))