from collections import defaultdict

text = list(input())
dic = defaultdict(int)
for i in text:
    dic[i] += 1

answer = []
for key, value in dic.items():
    answer.append([key, value])

answer.sort(key = lambda x : x[1])

if answer[0][1] == 1:
    print(answer[0][0])
else:
    print(None)