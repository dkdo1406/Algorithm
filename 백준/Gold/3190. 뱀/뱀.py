from collections import deque
N = int(input())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
apple = []
M = int(input())
for _ in range(M):
    r, c = list(map(int, input().split()))
    graph[r][c] = 10
T = int(input())
time = dict()
for _ in range(T):
    t, spin = list(input().split())
    if spin == 'L':
        time[int(t)] = -1
    else:
        time[int(t)] = 1

graph[1][1] = 1
dr = [0,1,0,-1]
dc = [1,0,-1,0]
direction = 0
answer = 0
q = deque()
q.append([1, 1])
while q:
    r, c = q.popleft()
    q.appendleft([r,c])
    if answer in time:
        direction += time[answer]
    if direction < 0:
        direction = 3
    if direction > 3:
        direction = 0
    nr = r + dr[direction]
    nc = c + dc[direction]
    answer += 1
    if nr < 1 or nr > N or nc < 1 or nc > N or graph[nr][nc] == 1:
        break
    if graph[nr][nc] != 10:
        r, c = q.pop()
        graph[r][c] = 0
    graph[nr][nc] = 1
    q.appendleft([nr, nc])
print(answer)
