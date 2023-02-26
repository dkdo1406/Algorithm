import sys
input = lambda : sys.stdin.readline()
N, K = list(map(int, input().split()))

arr = list(map(int, input().split()))
ans = 0
while max(arr) - min(arr) > K:
    ans += 1
    # 1. 가장 작은 물고기가 들어있는 어항에 +1
    min_val = min(arr)
    for i in range(len(arr)):
        if arr[i] == min_val:
            arr[i] += 1

    # 2. 어항쌓기. 가장 왼쪽부터 1개씩 증가하며 시계방향으로 90도 회전시켜 위에 쌓는다.
    # 2-1 d를 찾는다.
    # 2-2 어항을 쌓는 그래프를 만든다.
    temp = int(N ** 0.5)
    if temp % 2 == 0:
        if N - temp ** 2 - temp + 1 < 0:
            d = 0
        else:
            d = 3
    else:
        if N - temp ** 2 - temp + 1 < 0:
            d = 2
        else:
            d = 1

    graph = [[-10 for _ in range(20)] for _ in range(10)]

    def draw_graph(d, temp):
        global graph
        dr = [0, 1, 0, -1]
        dc = [-1, 0, 1, 0]
        r, c = 4, 5
        ptr = 0
        graph[r][c] = arr[ptr]
        ptr += 1
        start = 1
        if d % 2 == 1:
            stop = True
        else:
            stop = False
        while ptr < N:
            for i in range(2):
                for _ in range(start):
                    r += dr[d]
                    c += dc[d]
                    graph[r][c] = arr[ptr]
                    ptr += 1
                d = (d + 1) % 4
                if start == temp and stop:
                    for i in range(ptr, N):
                        r += dr[d]
                        c += dc[d]
                        graph[r][c] = arr[i]
                    return
            start += 1
            if start == temp and not stop:
                for i in range(ptr, N):
                    r += dr[d]
                    c += dc[d]
                    graph[r][c] = arr[i]
                return

    draw_graph(d, temp)

    r, c = N // 2 - 1, N // 2 - 1
    cnt = N - 1
    cnt -= 1

    # 3. 모든 인접한 어항에 대해 물고기 차이를 5로나눈 몫을 d라고 하자. d가 0보다 크면 두 어항 중 물고기가 많은 곳에서 적은곳으로 d마리만큼 이동
    def move(r, c, n, m):
        global temp_graph
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= n or nc < 0 or nc >= m or graph[nr][nc] == -10:
                continue
            if graph[r][c] - graph[nr][nc] > 4:
                result = (graph[r][c] - graph[nr][nc]) // 5
                temp_graph[r][c] -= result
                temp_graph[nr][nc] += result
            elif graph[nr][nc] - graph[r][c] > 4:
                result = (graph[nr][nc] - graph[r][c]) // 5
                temp_graph[r][c] += result
                temp_graph[nr][nc] -= result

    temp_graph = [[0 for _ in range(20)] for _ in range(10)]
    for r in range(10):
        for c in range(20):
            if graph[r][c] != -10:
                    move(r, c, 10, 20)
    for r in range(10):
        for c in range(20):
            graph[r][c] += temp_graph[r][c] // 2
    arr = []
    for c in range(20):
        for r in range(9, -1, -1):
            if graph[r][c] != -10:
                arr.append(graph[r][c])

    graph = [[] for _ in range(4)]

    str = N // 4
    new_arr = []
    for i in range(0,N,N//4):
        new_arr.append(arr[i:str])
        str += N // 4
    order = [2,1,0,3]

    for r in range(4):
        if r % 2 == 0:
            graph[r] = list(reversed(new_arr[order[r]]))
        else:
            graph[r] = new_arr[order[r]]

    temp_graph = [[0 for _ in range(N // 4)] for _ in range(4)]
    for r in range(4):
        for c in range(N // 4):
            move(r, c, 4, N//4)

    for r in range(4):
        for c in range(N // 4):
            graph[r][c] += temp_graph[r][c] // 2

    arr = []
    for c in range(N//4):
        for r in range(3, -1, -1):
            arr.append(graph[r][c])
print(ans)