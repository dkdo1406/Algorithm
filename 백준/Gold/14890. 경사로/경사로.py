from collections import deque
N, L = list(map(int, input().split()))

graph = [list(map(int, input().split())) for _ in range(N)]

# 1. 지나가려면 길의 높이가 같아야 한다.
# 1-1 경사로에 사다리를 놓아 길을 이을 수 있다.
# 2. 경사로의 높이는 항상 1이며 길이는 L이다. 만약 L이 2일 경우 1에서 2로 가려면 1이 총 3개 있어야 갈 수 있다.
# 2-1 경사로를 놓을 높이는 늘 같아야 한다.
# 2-2 경사로를 여러개 쌓을 수 없다.

# 지나가는 길이란 끝에서 끝으로 이동이 가능하다는 뜻이다.
ans = 0
def r_bfs(R, C):
    global ans
    q = deque()
    q.append((R, C))
    h = graph[R][C]
    cnt = 0
    while q:
        r, c = q.popleft()
        if int(abs(h - graph[r][c])) > 1:
            return
        if graph[r][c] == h:
            cnt += 1
            if c + 1 != N:
                q.append((r, c + 1))
        else:
            if h > graph[r][c]:
                cnt = -1
                curr_h = graph[r][c]
                nc = c - 1
                for _ in range(L):
                    nc += 1
                    if nc >= N or graph[r][nc] != curr_h:
                        return
                q.append((r, nc))
            else:
                if cnt < L:
                    return
                else:
                    cnt = 0
                    q.append((r, c))
                    curr_h = graph[r][c]
            h = curr_h
    ans += 1

def c_bfs(R, C):
    global ans
    q = deque()
    q.append((R, C))
    h = graph[R][C]
    cnt = 0
    while q:
        r, c = q.popleft()
        if int(abs(h - graph[r][c])) > 1:
            return
        if graph[r][c] == h:
            cnt += 1
            if r + 1 != N:
                q.append((r + 1, c))
        else:
            if h > graph[r][c]:
                cnt = -1
                curr_h = graph[r][c]
                nr = r - 1
                for _ in range(L):
                    nr += 1
                    if nr >= N or graph[nr][c] != curr_h:
                        return
                q.append((nr, c))
            else:
                if cnt < L:
                    return
                else:
                    cnt = 0
                    q.append((r, c))
                    curr_h = graph[r][c]
            h = curr_h
    ans += 1



for i in range(N):
    r_bfs(i, 0)
    c_bfs(0, i)

print(ans)