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
print(make1(n))