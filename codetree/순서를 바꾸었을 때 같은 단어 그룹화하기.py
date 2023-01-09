from collections import defaultdict
n = int(input())
dic = defaultdict(int)
for _ in range(n):
    text = list(input())
    text.sort()
    textSort = ''.join(text)
    dic[textSort] += 1

answer = []
for key, value in dic.items():
    answer.append([key, value])

answer.sort(key = lambda x : x[1], reverse= True)
print(answer[0][1])

