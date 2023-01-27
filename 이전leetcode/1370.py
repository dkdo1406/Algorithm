"""
1. 그냥 하나하나 비교하기
2. set함수 사용해서 빠르게하기
3. Counter함수 사용해서 계산
"""
import collections
import string

s = "adasdfsdbs"
cnt, ans, asc  = collections.Counter(s), [], True
while len(ans) < len(s):  # if not finish.
    for i in range(26):  # traverse lower case letters.
        c = string.ascii_lowercase[i if asc else ~i]  # in ascending/descending order.
        print(c)
        if cnt[c] > 0:  # if the count > 0.
            ans.append(c)  # append the character.
            cnt[c] -= 1  # decrease the count.
    asc = not asc  # change direction.
print(''.join(ans))
exit()
tmp = list(s)
answer = []
while len(answer)!=len(s):
    ns = sorted(set(tmp))
    for i in ns:
        answer.append(i)
        tmp.remove(i)
    ns = sorted(set(tmp),reverse=True)
    for i in ns:
        answer.append(i)
        tmp.remove(i)
print(''.join(answer))