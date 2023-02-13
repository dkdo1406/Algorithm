from collections import defaultdict
from collections import deque
N, M = list(map(int, input().split()))

graph = [list(map(int, input().split())) for _ in range(N)]

skill = [list(map(int, input().split())) for _ in range(M)]

shark = [N//2, N//2]

ans = defaultdict(int)

def magic(dir, ran):
    dr = [0, -1, 1, 0, 0]
    dc = [0, 0, 0, -1, 1]
    r, c = shark
    for i in range(1, ran + 1):
        nr = r + dr[dir] * i
        nc = c + dc[dir] * i
        graph[nr][nc] = 0

def graph_sort():

    "11, 22, 33, 44, 55"
    "왼, 아래, 오른쪽, 위"
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]
    arr = []
    i = 0
    r, c = shark
    re_cnt = 0
    cnt = 1
    while re_cnt < (N ** 2) - N:
        for _ in range(2):
            for count in range(cnt):
                r += dr[i%4]
                c += dc[i%4]
                re_cnt += 1
                if graph[r][c] != 0:
                    arr.append(graph[r][c])
            i += 1
        cnt += 1
    for count in range(cnt - 1):
        r += dr[i%4]
        c += dc[i%4]
        re_cnt += 1
        if graph[r][c] != 0:
            arr.append(graph[r][c])


    while True:
        copy_arr = []
        j = k = 0
        while k < len(arr):
            k += 1
            if k == len(arr):
                if k - j > 3:
                    ans[arr[j]] += k - j
                else:
                    copy_arr += arr[j:k]
            else:
                if arr[j] == arr[k]:
                    continue
                else:
                    if k - j > 3:
                        ans[arr[j]] += k - j
                    else:
                        copy_arr += arr[j:k]
                    j = k
        if arr == copy_arr:
            break
        arr = copy_arr
    return arr

def countMarble(arr):
    new_arr = deque()

    j = k = 0
    while k < len(arr):
        k += 1
        if k == len(arr):
            new_arr.append(k - j)
            new_arr.append(arr[j])

        else:
            if arr[j] != arr[k]:
                new_arr.append(k - j)
                new_arr.append(arr[j])
                j = k

    return new_arr
def addGraph(arr):
    global graph
    graph = [[0 for _ in range(N)] for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]
    i = 0
    r, c = shark
    re_cnt = 0
    cnt = 1
    while re_cnt < (N ** 2) - N:
        for _ in range(2):
            for count in range(cnt):
                r += dr[i%4]
                c += dc[i%4]
                re_cnt += 1
                if not arr:
                    return
                graph[r][c] = arr.popleft()
            i += 1
        cnt += 1
    if arr:
        for count in range(cnt - 1):
            r += dr[i%4]
            c += dc[i%4]
            re_cnt += 1
            if not arr:
                return
            graph[r][c] = arr.popleft()



for i in range(M):
    dir, ran = skill[i]
    magic(dir, ran)
    arr = graph_sort()
    new_arr = countMarble(arr)
    addGraph(new_arr)
res = 0
for key, value in ans.items():
    res += key * value
print(res)


