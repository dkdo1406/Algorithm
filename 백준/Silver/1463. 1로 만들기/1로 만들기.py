n = int(input())

dp = [0 for i in range(n+1)]

# 1일경우 횟수는 0이기 때문에 2부터 시작
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[n])