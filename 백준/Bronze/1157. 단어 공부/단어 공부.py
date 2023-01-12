from collections import defaultdict
import sys
input = lambda : sys.stdin.readline()

text = input()
dic = defaultdict(int)
for i in text:
    if i.isalpha():
        dic[i.upper()] += 1
sort_dic = sorted(dic.items(), key = lambda x: x[1], reverse= True)
answer = sort_dic[0][0]
if len(sort_dic) > 1 and sort_dic[0][1] == sort_dic[1][1]:
    answer = "?"
print(answer)