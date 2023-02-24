from collections import deque
N, M = list(map(int, input().split()))
robot = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(N)]

# 1 현재칸이 청소안되어 있으면 청소한다.
# 2-1. 빈칸 없을 때 : 후진할 수 있으면 한칸 후진, 만약 후진칸이 벽이면 종료
# 2-2. 빈칸 있을 때 : 반시계반향 회전, 만약 청소안한 칸이면 한칸 전진
# 0은 청소안한 칸 1은 벽
# d의 0은 위, 1은 오른쪽, 2는 밑, 3은 왼쪽

dr = [-1,0,1,0]
dc = [0,1,0,-1]


def clean():
    r, c, d = robot
    q = deque()
    q.append((r,c,d))
    graph[r][c] = -1
    ans = 1
    while q:
        r,c,d = q.popleft()
        for _ in range(4):
            d = (4 + d - 1) % 4
            nr = r + dr[d]
            nc = c + dc[d]
            if nr < 1 or nr >= N - 1 or nc < 1 or nc >= M - 1 or graph[nr][nc] == 1 or graph[nr][nc] == -1:
                continue
            ans += 1
            graph[nr][nc] = -1
            q.append((nr, nc, d))
            break

            # 여기서 뭔짓을 한다.
        # 1. 모두가 청소되어 있다.
        if not q:
            nr = r + dr[(d + 2) % 4]
            nc = c + dc[(d + 2) % 4]
            if graph[nr][nc] == 1:
                break
            q.append((nr, nc, d))
    return ans
print(clean())
