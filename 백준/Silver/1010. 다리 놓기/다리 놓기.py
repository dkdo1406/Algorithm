import sys
input = lambda : sys.stdin.readline()
T = int(input())
result = []
for _ in range(T):
    N,M = map(int,input().split(' '))
    if N==0:
        result.append(0)
        continue
    answer = 1
    for i in range(M,M-N,-1):
        answer *=i
    for i in range(1,N+1):
        answer //=i
    result.append(answer)
for i in result:
    print(i)