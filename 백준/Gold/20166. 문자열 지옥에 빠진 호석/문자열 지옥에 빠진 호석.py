import sys
from collections import deque

n, m, k = list(map(int, sys.stdin.readline().split()))

arr = []
for u in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))

like_dict = dict()


def bfs(i: int, j: int):
    # 남, 동, 북, 서 , 남동, 남서, 북동, 북서
    dx = [1, 0, -1, 0, 1, 1, -1, -1]
    dy = [0, 1, 0, -1, 1, - 1, 1, -1]

    queue = deque()
    # (x,y,이어 붙일 문자열)
    queue.append((i, j, arr[i][j]))

    while queue:
        x, y, string = queue.popleft()

        # 아예 bfs를 한번만 해서 미리 dict에 등록해두자.
        if string not in like_dict:
            like_dict[string] = 1
        else:
            like_dict[string] += 1

        #  문자열의 길이가 Loop 종료 조건에 해당한다.
        if len(string) >= 5:
            continue

        for d in range(8):
            adj_x = x + dx[d]
            adj_y = y + dy[d]

            # 환형 처리
            if adj_x == n:
                adj_x = 0
            elif adj_x == -1:
                adj_x = n - 1

            if adj_y == m:
                adj_y = 0
            elif adj_y == -1:
                adj_y = m - 1

            queue.append((adj_x, adj_y, string + arr[adj_x][adj_y]))


answer_list = []

# 아예 bfs를 한번만 해서 미리 dict에 등록해두자.
for a in range(n):
    for b in range(m):
        bfs(a, b)

for u in range(k):
    like = sys.stdin.readline().rstrip()

    if like in like_dict:
        answer_list.append(like_dict[like])
    else:
        answer_list.append(0)

for answer in answer_list:
    print(answer)