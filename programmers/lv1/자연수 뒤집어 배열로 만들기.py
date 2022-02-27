"""
https://programmers.co.kr/learn/courses/30/lessons/12932
"""

n = 12345
# result = [5,4,3,2,1]
answer = []
for i in range(len(str(n))):
    answer.append(int(str(n)[i]))
answer.reverse()
print(answer)