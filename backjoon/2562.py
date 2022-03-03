"""
https://www.acmicpc.net/problem/2562
3
29
38
12
57
74
40
85
61
result
85
8
"""
import sys
input = lambda : sys.stdin.readline()
answer = 0
line = 0
for i in range(1,10):
    n = int(input())
    if answer <n:
        answer = n
        line = i
print(answer)
print(line)