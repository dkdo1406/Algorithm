"""
ABRACADABRA
ECADADABRBCRDARA
가장 긴 공통문자열 길이 찾기
시간복잡도 O(n)으로 풀어야 함
"""
import sys
input = lambda : sys.stdin.readline()
A = input()
B = input()
count = 0
if len(A)<len(B):
    short = A
    long = B
else:
    short = B
    long = A

lt = 0
rt = 0
while rt<len(short)-1:
    rt+=1
    if short[lt:rt] in long:
        count = max(rt-lt, count)
    else:
        lt+=1
print(count)