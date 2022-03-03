"""
https://programmers.co.kr/learn/courses/30/lessons/49191?language=python3

n=5
results	=[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
return 2

2번 선수는 [1, 3, 4] 선수에게 패배했고 5번 선수에게 승리했기 때문에 4위입니다.
5번 선수는 4위인 2번 선수에게 패배했기 때문에 5위입니다.

한명이 n-1번 싸워보면 순위가 무조건 결정된다.
a가 b를 이기고 b가 c를 이기면 a는 c를 이긴것과 같다.
score[a][b] = 1
score[b][a] = -1
그래프 안에 있는 내용을 모두 탐색하여 시작지점보다 작은 수를 위와 같은 방법으로 score에 저장
마지막에 score에서 탐색을 안한 부분인 0의 개수가 2이면 n-1번 경기를 했으므로 answer+=1을 함
"""
n=5
results	=[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
graph = [[] for i in range(n+1)]
score = [[0]*(n+1) for i in range(n+1)]

answer=0
for win,lose in results:
    graph[win].append(lose)


def DFS(start,graph):
    visited = [False]*(n+1)
    visited[start]=True
    stack=[]
    stack.append(start)

    while stack:
        v = stack.pop()
        for i in graph[v]:
            if not visited[i]:
                visited[i]=True
                stack.append(i)
                score[start][i] = 1
                score[i][start] = -1
           
for i in range(1,n+1):
    DFS(i,graph)
for i in range(1,n+1):
    if score[i].count(0)==2:
        print(i)
        answer+=1
print(answer)
print(score)





print(graph)

# for i,j in results:
