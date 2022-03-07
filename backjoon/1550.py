"""
16진수를 10진수로 변환
파이썬은 int(A,진수)를 지원한다.
"""
s = input()
cnt = len(s)-1
dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
answer = 0
for i in s:
    if i in dic:
        answer += dic[i] * (16 ** cnt)
    else:
        answer += int(i) * (16 ** cnt)
    cnt -= 1
print(answer)

#이런....
print(int(input(),16))