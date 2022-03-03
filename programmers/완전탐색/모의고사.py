"""
https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3

핵심 : 1,2,3 수포자들이 찍는 순서를 계속 반복하게 만들기
deque에 rotate라는 함수를 이용함
rotate(int)인데 아무것도 안넣으면 +1처럼 행동, 양수일경우 오른쪽으로 민다. => 마치 stack같이
음수일경우 왼쪽으로 민다. => 마치 queue같이

"""
from collections import deque

a =[1, 2, 3, 4, 5]
b =[2, 1, 2, 3, 2, 4, 2, 5]
c =[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
a = deque(a)
b = deque(b)
c = deque(c)
result = [0]*3
answer=[]
for i in answers:
    if i==a[0]:
        result[0]+=1
    if i==b[0]:
        result[1]+=1
    if i==c[0]:
        result[2]+=1
    a.rotate(-1)
    b.rotate(-1)
    c.rotate(-1)
for i,j in enumerate(result):
    if j==max(result):
        answer.append(i+1)