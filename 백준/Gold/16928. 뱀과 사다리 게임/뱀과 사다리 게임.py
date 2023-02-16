from collections import defaultdict
from collections import deque
N, M = list(map(int, input().split()))
ladders = defaultdict(int)
snakes = defaultdict(int)
for _ in range(N):
    start, end = list(map(int, input().split()))
    ladders[start] = end
for _ in range(M):
    start, end = list(map(int, input().split()))
    snakes[start] = end


dp = [-1 for i in range(101)]

def bfs():
    q = deque()
    q.append((1, 0))
    dp[1] = 0
    while q:
        here, L = q.popleft()
        for i in range(1,7):
            move = here + i
            if move > 100:
                break
            if dp[move] != -1 and dp[move] <= L:
                continue
            dp[move] = L + 1
            if move in ladders:
                q.append((ladders[move], L + 1))
                dp[ladders[move]] = L + 1
            elif move in snakes:
                q.append((snakes[move], L + 1))
                dp[snakes[move]] = L + 1
            else:
                q.append((move, L + 1))
bfs()
print(dp[100])