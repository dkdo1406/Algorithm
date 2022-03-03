"""
https://leetcode.com/problems/reorder-data-in-log-files/

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:
Letter-logs : 소문자 영단어로 조합(식별자는 제외)
Digit-logs: 숫자로 조합(식별자는 제외)
letter-logs는 Digit-logs 앞에 온다.
letter-logs는 안에 문자 우선순위대로 식별자 정렬
Digit-logs는 들어온순서대로


Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

lambda로 정렬 하기
"""
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Letter_logs = []
Digit_logs = []
for i in logs:
    s = i.split(' ')
    if s[1].isalpha():
        Letter_logs.append(i)
    else:
        Digit_logs.append(i)

print(Letter_logs)
# Letter_logs.sort(key= lambda x : (x.split()[1:],x.split()[0]))
Letter_logs = sorted(Letter_logs,key= lambda x: (x.split()[1:],x.split()[0]))
print(Letter_logs)

"""
내방법
temp = {}
for i in logs:
    s = i.split()
    temp[s[0]] = ''.join((s[1:]))
for i in temp:
    if temp[i][0].isalpha():
        
print(temp)
"""


