"""
https://programmers.co.kr/learn/courses/30/lessons/42860?language=python3


name	return
"JEROEN"	56
"JAN"	23
"""
# 13 100 5
# a,b,c =    map(int,input().split())

from cmath import sqrt


a,b,c = 2147483646, 125, 2147483647
print(sqrt(2147483647))
print(46340**2)
print(pow(a,b,c))
if b ==0:
    print(a%c)
else:
    print((a**b)%c)

    print(a%c)
# number =[2,7]
# answer = []
# for i in number:
#     num = i
#     target =  format(i,'b')
#     a = format(num,'b')
#     print()
#     while True:
#         cnt=0
#         num+=1
#         print(target[:-1])
#         target = list(format(i,'b'))
#         a = list(format(num,'b'))
#         if len(target)!=len(a):
#             target.insert(0,0)
#         while target and cnt<5:
#             if target and target.pop()!=a.pop():
#                 cnt+=1
#         if cnt<3:
#             answer.append(num)
#             break
# print(answer)
# for i in range(1,12):
#     print(i,format(i,'b'))

