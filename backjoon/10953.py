import sys
input = lambda: sys.stdin.readline()
T = int(input())
for i in range(T):
    a,b = map(int,input().split(sep= ','))
    print(a+b)