from collections import defaultdict
N = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]
students = [list(map(int, input().split())) for _ in range(N ** 2)]

# 상하좌우 대각선 순으로 확장
dr = [0, -1, 1, 0]
dc = [-1, 0, 0, 1]

# 그래프에 좋아하는 학생이 있고 인접한 칸에 자리가 있다면 앉아야 한다.
# 인접한 칸 중 빈칸이 많은 칸
# 행번호 작은칸, 열번호 작은 칸
def chk1(arr, num):
    # 좋아하는 학생이 인접한 곳 찾기
    temp = defaultdict(int)
    for R, C in arr:
        for i in range(4):
            nr = R + dy[i]
            nc = C + dx[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            # 이것들이 아니면 모두 인접한값이기 때문에 값을 저장해준다.
            if graph[nr][nc] == 0:
                temp[(nr, nc)] += 1
    if not temp:
        # 그래프에 좋아하는 학생은 있지만 붙은자리가 없으면 chk2로 이동
        chk2([], num)
    # 인접한 값이 있을 경우 값을 기준으로 정렬을 해준다
    else:

        temp = sorted(temp.items(), key=lambda x: (-x[1],x[0][0],x[0][1]))
        # if num == 9:
        #     print(temp)
        # 인접한 칸의 중복 확인
        chkOverlap = []
        chkOverlap.append(temp[0][0])
        for i in range(len(temp)-1):
            if temp[i][1] == temp[i+1][1]:
                chkOverlap.append(temp[i+1][0])
            else:
                break
        # 인접한 칸에 한개있으면 우선순위에 의해
        if len(chkOverlap) == 1:
            graph[chkOverlap[0][0]][chkOverlap[0][1]] = num
            return
        else:
            # 그래프에 좋아하는 학생이 있지만 인접한 학생들이 있어 chk2로 이동해서 빈칸 확인
            chk2(chkOverlap, num)
            return

def chk2(arr, num):
    # 좌표가 전혀 없는 애는 모든칸 중 상하좌우를 살펴 빈칸이 좌표들을 찾는다.
    dict = defaultdict(int)
    if not arr:
        # 좋아하는 친구가 인접한 칸에 없으면 빈칸이 많은곳으로 자리를 정한다.
        for R in range(N):
            for C in range(N):
                if graph[R][C] == 0:
                    for i in range(4):
                        nx = R + dy[i]
                        ny = C + dx[i]
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue
                        if graph[nx][ny] == 0:
                            dict[(R,C)] += 1
    else:
        for R, C in arr:
            for i in range(4):
                nr = R + dy[i]
                nc = C + dx[i]
                if nr < 0 or nr >= N or nc < 0 or nc >= N or graph[nr][nc] != 0:
                    continue
                dict[(R,C)] += 1
    dict = sorted(dict.items(), key=lambda x: (-x[1],x[0][0],x[0][1]))
    if not dict:
        # 만약 빈칸이 모두 없으면 행 열이 작은곳으로 넣는다.
        for R in range(N):
            for C in range(N):
                if graph[R][C] == 0:
                    graph[R][C] = num
                    return
    else:
        graph[dict[0][0][0]][dict[0][0][1]] = num
        return

    dict = sorted(dict.item)
    chkOverlap = []
    chkOverlap.append(dict[0][0])
    # 빈칸의 중복 확인
    for i in range(len(dict) - 1):
        if dict[i][1] == dict[i + 1][1]:
            chkOverlap.append(dict[i+1][0])
        else:
            break
    # 빈칸개수가 만약 한개면 그냥 pass
    if len(chkOverlap) == 1:
        graph[chkOverlap[0][0]][chkOverlap[0][1]] = num
        return
    # 빈칸개수가 여러개면 행 열 우선순위로 정해서 넣는다.
    else:
        chkOverlap.sort(key=lambda x: (x[0], x[1]))
        graph[chkOverlap[0][1]][chkOverlap[0][0]] = num
        return

# 그래프에 좋아하는 학생이 있고 인접한 칸이 많은 자리
# 인접한 칸 중 빈칸이 많은 칸
# 행번호 작은칸, 열번호 작은 칸
for num,a,b,c,d in students:
    arr = []
    # [인접, 빈칸, R, C]
    like = [a,b,c,d]
    for R in range(N):
        for C in range(N):
            likeCnt = 0
            blankCnt = 0
            if graph[R][C] != 0:
                continue
            for i in range(4):
                nr = R + dr[i]
                nc = C + dc[i]
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue
                if graph[nr][nc] in like:
                    likeCnt += 1
                if graph[nr][nc] == 0:
                    blankCnt += 1
            # 한 배열안에 모두 넣어버린다.
            arr.append([likeCnt, blankCnt, R, C])
    # 우선순위 정렬
    # 인접한것은 큰순, 빈칸 큰순, R,C 는 작은 순
    arr.sort(key= lambda x: (-x[0], -x[1], x[2], x[3]))

    graph[arr[0][2]][arr[0][3]] = num


result = 0
score = [0, 1, 10, 100, 1000]
for R in range(N):
    for C in range(N):
        cnt = 0
        for student in students:
            num, a,b,c,d = student
            lst = [a, b, c, d]
            if num == graph[R][C]:
                for i in range(4):
                    nr = R + dr[i]
                    nc = C + dc[i]
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        continue
                    if graph[nr][nc] in lst:
                        cnt += 1

        result += score[cnt]
print(result)
# for i in graph:
#     print(i)
