import sys
input = lambda: sys.stdin.readline()

T = int(input())
result = []
for i in range(T):
    a,b = map(int,input().split())
    print(a+b)