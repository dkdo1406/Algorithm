"""
S 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 0 0 0 1
1 1 0 1 1 0 0
1 0 0 0 0 0 E
S에서 E로 가는 경우의 수 출력
상 하 좌 우를 갈 수 있음
위일경우 x는 0 y는 +1
내위치를 계속 반환하다가 새로운 경우의 수이면 출력 후 리턴
"""

graph = [list(map(int,input().split())) for i in range(7)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
visited = [False]*8
start = [0,0]
answer = 0
graph[0][0]=1
def DFS(x,y):
    global answer
    if graph[x][y]==graph[6][6]:
        answer+=1
        return
    else:
        for i in range(4):
            if x+dx[i]<0 or y+dy[i]<0 or x+dx[i]>6 or y+dy[i]>6:
                pass
            else:
                if graph[x+dx[i]][y+dy[i]]==0:
                    graph[x+dx[i]][y+dy[i]]=1
                    DFS(x+dx[i],y+dy[i])
                    graph[x+dx[i]][y+dy[i]]=0
DFS(0,0)
print(answer)