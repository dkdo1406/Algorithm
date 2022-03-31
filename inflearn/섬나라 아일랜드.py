"""
1로 이루어진 섬과 0인 바다가 있다.
섬의 개수를 구하라
"""
import collections
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
answer = 0
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
def DFS(x,y):
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<N and board[nx][ny]==1:
            board[nx][ny]=0
            DFS(nx,ny)
def BFS(x,y):
    q = collections.deque()
    q.append([x,y])
    while q:
        Vx,Vy = q.popleft()
        for i in range(8):
            nx = Vx + dx[i]
            ny = Vy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 1:
                board[nx][ny] = 0
                q.append([nx,ny])

for r in range(N):
    for c in range(N):
        if board[r][c] ==1:
            BFS(r,c)
            # DFS(r,c)
            board[r][c]=0
            answer+=1
print(answer)