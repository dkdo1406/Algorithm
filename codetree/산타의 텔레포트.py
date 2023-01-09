from collections import deque
C, R = list(map(int, input().split()))

graph = []
for i in range(R):
    graph.append(list(map(int, input().split())))

gift = []
for r in range(R):
    for c in range(C):
        if graph[r][c] == -2:
            gift.append(r)
            gift.append(c)

# 선물을 토대로 근처에 무엇이 있는지 확인
dr = [0,0,1,-1]
dc = [1,-1,0,0]
gift_teleport = []
goal_teleport = []
def find_gift():
    q = deque()
    q.append(gift)
    visited = [gift]
    while q:
        r,c = q.popleft()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if nr < 0 or nr >= R or nc < 0 or nc >= C or graph[nr][nc] == -1 or graph[nr][nc] == -2 or [nr,nc] in visited:
                continue
            visited.append([nr, nc])
            if graph[nr][nc] > 10:
                if [graph[nr][nc], nr, nc] not in gift_teleport:
                    gift_teleport.append([graph[nr][nc], nr, nc])
            q.append([nr, nc])

def find_goal():
    q = deque()
    q.append([R-1,C-1])
    visited = [R-1,C-1]
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if nr < 0 or nr >= R or nc < 0 or nc >= C or graph[nr][nc] == -1 or [nr,nc] in visited:
                continue
            visited.append([nr, nc])
            if graph[nr][nc] > 10:
                if [graph[nr][nc], nr, nc] not in goal_teleport:
                    goal_teleport.append([graph[nr][nc], nr, nc])
            if graph[nr][nc] == -2:
                # 바로 시작
                pass
            q.append([nr, nc])

find_gift()
