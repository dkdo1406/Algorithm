from collections import defaultdict

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
dic = defaultdict(int)
for i in arr:
    dic[i] += 1
answer = []
for key, value in dic.items():
    answer.append([key, value])
answer.sort(key = lambda x : (x[1], x[0]), reverse = True)

for i in range(k):
    print(answer[i][0], end = ' ')
