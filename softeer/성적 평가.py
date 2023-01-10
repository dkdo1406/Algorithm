import sys
from collections import defaultdict
input = lambda : sys.stdin.readline()
n = int(input())

answer = [0] * n

def rank(arr):
    dic = defaultdict(list)
    for i in range(n):
        dic[arr[i]] += [i]
    sort_dic = sorted(dic.items(), reverse= True)
    dic = dict()
    result = 1
    for score, r in sort_dic:
        dic[score] = result
        result += len(r)
    for i in arr:
        print(f"{dic[i]}", end= ' ')
    print()
for _ in range(3):
    arr = list(map(int, input().split()))
    for i in range(n):
        answer[i] += arr[i]
    rank(arr)
rank(answer)

