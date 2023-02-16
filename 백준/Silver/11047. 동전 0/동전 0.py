N, K = list(map(int, input().split()))
money = []

for _ in range(N):
    M = int(input())
    if M > K:
        break
    money.append(M)
ans = 0
for _ in range(len(money)):
    coin = money.pop()
    if coin <= K:
        cnt = K // coin
        K -= coin * cnt
        ans += cnt
    if K == 0:
        break
print(ans)
