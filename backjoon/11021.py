import sys

input = lambda: sys.stdin.readline()
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    # print("Case #%d: %d" %(i+1, a+b))
    print('Case #{0}: {1}'.format(i+1, a+b))
