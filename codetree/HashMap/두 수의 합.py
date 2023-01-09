from collections import defaultdict
n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
dic = defaultdict(int)
answer = 0
for i in arr:
    dic[k - i] += 1

for index, i in enumerate(arr):
    if i in dic and dic[i] > 0:
        dic[k - i] -= 1
        answer += dic[i]

print(answer)