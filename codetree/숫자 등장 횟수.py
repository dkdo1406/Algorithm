from collections import defaultdict
n, m = list(map(int, input().split()))
arrN = list(map(int, input().split()))
arrM = list(map(int, input().split()))

dicN = defaultdict(int)
answer = []
for i in arrN:
    dicN[i] += 1
for i in arrM:
    if i in dicN:
        answer.append(dicN[i])
    else:
        answer.append(0)
for i in answer:
    print(i, end= ' ')