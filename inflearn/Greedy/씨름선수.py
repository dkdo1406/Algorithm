# 앞 지원자보다 키와 몸무게가 모두 높은 경우 탈락 아니면 선발

import sys
import math

def combi(n,r):
    p = n
    for i in range(1,r):
        p = p * (n - i) / i
    else:
        p = p / (i+1)
    return p
print(combi(5,2))
exit()
input = lambda : sys.stdin.readline()
N = int(input())
A = [list(map(int,input().split())) for i in range(N)]
A.sort()
A.sort(key = lambda x: -(x[1], x[0]))
print(N)
print(A)
# 그리디는 현재 시점에서 최선을 선택하는 것이다.

# for i in range(N):
n = 5
import math
