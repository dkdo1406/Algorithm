from collections import deque
N, K = list(map(int, input().split()))
graph = deque()

A = list(map(int, input().split()))
for i in range(2*N):
    graph.append([-1,A[i]])

def check():
    global graph, K
    cnt = 0
    for robot,life in graph:
        if life == 0:
            cnt += 1
    if cnt >= K:
        return True

def rotation():
    global graph, N, K
    result = 1
    robots = deque()
    # 1. 모든 컨테이너 회전(로봇들만 회전한다. 이때, 라이프는 감소하지 않음)
    while True:
        if len(robots) != 0:
            for _ in range(len(robots)):
                robot = robots.popleft()
                if robot+1 >= N-1:
                    graph[robot][0] = -1
                    continue
                robots.append((robot+1)%len(graph))
                graph[robot][0] = robot+1
        temp = graph.pop()
        graph.appendleft(temp)

        # 2. 올라간 순서대로 로봇 걸어가기 (걸어가면 피로도 깎인다)
        if len(robots) != 0:
            for _ in range(len(robots)):
                robot = robots.popleft() #아장아장
                if graph[(robot+1) % N][0] != -1 or graph[(robot+1) % N][1] == 0: # 로봇 X, 라이프 0이상
                    robots.append(robot)
                    continue
                if robot+1 >= N-1: #로봇이 내리는곳으로 이동하면
                    graph[robot][0] = -1
                    graph[robot+1][1] -= 1
                else: # 로봇의 범위가 앞이면
                    graph[(robot+1) % N] = [robot+1, graph[(robot+1) % N][1] - 1]
                    graph[robot][0] = -1
                    robots.append(robot+1)

        # 3. 올리는 칸에 내구도 0 아니면 로봇 올리기
        if graph[0][0] == -1 and graph[0][1] != 0:
            graph[0][0] = 0
            graph[0][1] -= 1
            robots.append(0)

        #4. 체크하기
        if check():
            print(result)
            break
        result += 1
rotation()
