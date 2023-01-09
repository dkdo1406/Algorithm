N = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]
students = [list(map(int, input().split())) for _ in range(N ** 2)]

# 상하좌우 대각선 순으로 확장
dr = [0, -1, 1, 0]
dc = [-1, 0, 0, 1]

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