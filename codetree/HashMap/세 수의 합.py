from collections import defaultdict
n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
dic = defaultdict(int)
answer = 0

for i in range(n-2):
    for j in range(i+1, n):
        dic[arr[j]] += 1
    for j in range(i+1, n):
        dic[arr[j]] -= 1
        answer += dic[k - (arr[i] + arr[j])]

print(answer)