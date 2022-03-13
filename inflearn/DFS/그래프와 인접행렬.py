"""
1.무방향 그래프
ex) 도시와 도시가 연결, 양쪽으로 이동가능
1-2-5
| |
3-4

간선
1 2
1 3
2 4
3 4
2 5
간선을 2차원 배열로 graph[a][b]=1,graph[b][a]=1 이렇게 두개다 체크한다.

2.방향 그래프
이동하는 방향이 존재
1->2->5
1->3->4
3에서 1로는 불가능
간선
1 2
1 3
2 4
3 4
2 5
graph[a][b]=1만 한다. 행->열로 이동한다.

3. 가중치 방향그래프
1번에서 2번으로 이동하는데 비용이 2다.
1->2->5
 2  5
graph[1][2]=2
graph[2][5]=5
graph[a][b]=c 로 표현

1에서 N까지 가는 모든 경로 가지 수 출력
5 9
1 2
1 3
1 4
2 1
2 3
2 5
3 4
4 2
4 5
"""
#방향 그래프
import collections

N,M = map(int,input().split())
graph = [[] for i in range(N+1)]
visited = [False]*(N+1)
visited[1]=True
answer =0
for i in range(M):
    start,end = map(int,input().split())
    graph[start].append(end)
def find_N(v,n):
    global answer,graph,visited
    if v==n:
        answer+=1
    else:
        for i in graph[v]:
            if not visited[i]:
                visited[i]=True
                find_N(i,n)
                visited[i]=False




print(find_N(1,N))
print(graph)
print(answer)
