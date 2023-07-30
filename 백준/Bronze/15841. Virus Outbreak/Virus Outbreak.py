dp = [0] * 491
dp[1] = 1
dp[2] = 1
for i in range(3, 491):
    dp[i] = dp[i-1] + dp[i - 2]

while True:
    time = int(input())
    if time == -1: break
    print(f"Hour {time}: {dp[time]} cow(s) affected")