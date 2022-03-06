"""
2 3
AB CDE
이름궁합 테스트
알파벳당 획수에 따라\

좀 더 머리를 써서 다시 해보자
"""

import sys
input = lambda : sys.stdin.readline()
N,M = map(int,input().split())
A,B= input().split()

alpha = {'A' : 3, 'B':2, 'C': 1,'D': 2,'E':4,'F':3, 'G':1,'H':3,'I':1,'J':1,'K':3,'L':1,'M':3,'N':2,'O':1,'P':2,'Q':2,'R':2,'S':1,'T':2,
       'U':1,'V':1,'W':1,'X':2,'Y':2,'Z':1}

lt=0
goong = []
while lt<max(N,M):
    if lt<min(N,M):
        goong.append(A[lt])
        goong.append(B[lt])
    else:
        if N>M:
            goong.append(A[lt])
        else:
            goong.append(B[lt])
    lt+=1
love = [alpha[i] for i in goong]
count=0
while len(love)>2:
    count+=1
    love = [love[i] + love[i + 1] if love[i]+love[i+1]<10 else (love[i]+love[i+1])%10 for i in range(len(love) - 1)]
print(str(love[0]*10+love[1])+'%')

