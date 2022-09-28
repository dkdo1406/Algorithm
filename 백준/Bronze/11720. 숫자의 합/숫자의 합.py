import sys
input = lambda: sys.stdin.readline()
T = int(input())
a = list(input())
answer = 0
for i in range(T):
    answer += int(a[i])
print(answer)