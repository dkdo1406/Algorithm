import sys
input = lambda : sys.stdin.readline()
N, M = list(map(int, input().split()))
arr = list(map(int, input().split()))
lst = [list(map(int, input().split())) for _ in range(M)]
dp = [0 for _ in range(len(arr) + 1)]
for i in range(len(arr)):
    dp[i+1] = arr[i] + dp[i]

for s, e in lst:
    print(dp[e] - dp[s-1])