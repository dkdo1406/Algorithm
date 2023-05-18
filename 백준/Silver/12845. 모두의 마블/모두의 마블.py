import sys
input = lambda: sys.stdin.readline()
n = int(input())
level = list(map(int, input().split()))
ans = 0
level.sort(reverse=True)
for i in range(1, n):
    ans += level[i] + level[0]

print(ans)