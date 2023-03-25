import sys
input = lambda : sys.stdin.readline()
T = int(input())
for _ in range(T):
    a, b = list(map(int, input().split()))
    print(a + b)