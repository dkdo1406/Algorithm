s = input()
dic = dict()
for i in range(len(s)):
    if s[i] not in dic:
        dic[s[i]] = i

for i in range(97, 123):
    if chr(i) in dic:
        print(dic[chr(i)], end= ' ')
    else:
        print(-1, end= ' ')
