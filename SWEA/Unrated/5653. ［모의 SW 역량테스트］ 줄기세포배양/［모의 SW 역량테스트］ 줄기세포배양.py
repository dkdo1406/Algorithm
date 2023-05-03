from collections import deque
T = int(input())

for test_case in range(1, T + 1):
    N, M, K = list(map(int, input().split()))
    ans = 0
    sample = []
    cell_graph = [[0 for _ in range(400 + M)] for _ in range(400 + N)]
    active_cell = [[] for _ in range(11)]
    sleep_cell = [[] for _ in range(11)]

    can_spread = [False for _ in range(11)]
    active_dead = [0 for _ in range(11)]
    sleep_active = [0 for _ in range(11)]

    for _ in range(N):
        sample.append(list(map(int, input().split())))

    for r in range(N):
        for c in range(M):
            if sample[r][c] > 0:
                sleep_cell[sample[r][c]].append([200 + r, 200 + c])
                cell_graph[200 + r][200 + c] = -1
                sleep_active[sample[r][c]] = sample[r][c] - 1

    q = deque()
    for i in range(10, 0, -1):
        if sleep_cell[i]:
            q.append(i)

    def spread(cell):
        cnt = False
        for r, c in active_cell[cell]:
            for i in range(4):
                nr = dr[i] + r
                nc = dc[i] + c
                if cell_graph[nr][nc] == -1:
                    continue
                cell_graph[nr][nc] = -1
                sleep_cell[cell].append([nr, nc])
                sleep_active[cell] = cell - 1
                cnt = True
        return cnt

    dr = [0,0,-1,1]
    dc = [1,-1,0,0]
    for k in range(1, K+1):
        n = len(q)
        for _ in range(n):
            cell = q.popleft()
            if not active_cell[cell] and not sleep_cell[cell]:
                continue
            if can_spread[cell]:
                if active_cell[cell]:
                    if spread(cell):
                        can_spread[cell] = False
                    active_dead[cell] -= 1
            else:
                if sleep_active[cell] == 0:
                    active_cell[cell].extend(sleep_cell[cell])
                    sleep_cell[cell].clear()
                    can_spread[cell] = True
                    active_dead[cell] = cell

                elif sleep_active[cell] > 0:
                    sleep_active[cell] -= 1
                    active_dead[cell] -= 1
            if active_dead[cell] == 0:
                active_cell[cell].clear()
            q.append(cell)

    while q:
        i = q.popleft()
        ans += len(active_cell[i])
        ans += len(sleep_cell[i])

    print(f"#{test_case} {ans}")
