"""
피보나치수열 구현 방법들
fib_1 : 기본형
fib_2 : 메모이제이션
fib_3 : 타뷸레이션(top_down)
"""
import collections
n = 4
def fib_1(n):
    if n<=1:
        return n
    else:
        return fib_1(n-1)+fib_1(n-2)

dp = collections.defaultdict(int)
def fib_2(n):
    if n<=1:
        return n
    if dp[n]:
        return dp[n]
    dp[n]= fib_2(n-1) + fib_2(n-2)
    return dp[n]

dp = collections.defaultdict(int)
def fib_3(n):
    dp[1] = 1

    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(fib_1(n))
print(fib_2(n))
print(fib_3(n))