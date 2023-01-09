from collections import defaultdict
n = int(input())
dic = defaultdict(int)
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr3 = list(map(int, input().split()))
arr4 = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        dic[arr1[i] + arr2[j]] += 1

answer = 0
for i in range(n):
    for j in range(n):
        if -(arr3[i] + arr4[j]) in dic:
            answer += dic[-(arr3[i] + arr4[j])]

print(answer)