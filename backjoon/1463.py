"""
3으로 나눠지면 3으로 나눈다
2로 나눠지면 2로나눈다
없으면 -1을 한다.
정수 N을 1로 만드는 최소 횟수
규칙 찾아서 점화식 만든 후 가장 작은값 리턴
가장 짧은 경우의 수 1일경우 0, 2일경우 1, 3일경우 1, 4일경우 [2]+1 or [3]+1
"""
import collections
n = int(input())
dp = collections.defaultdict(int)


def make1(n):
    if n==1:
        return 0
    for i in range(2,n+1):
        dp[i] = dp[i - 1] + 1
        if i%3==0 and dp[i]>dp[i//3]+1:
            dp[i]=dp[i//3]+1
        if i%2==0 and dp[i]>dp[i//2]+1:
            dp[i] = dp[i // 2] + 1

    return dp[n]

dp = [0, 0, 1, 1]
for i in range(4, n + 1):
    dp.append(dp[i - 1] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
print(dp[n])

print(make1(n))

