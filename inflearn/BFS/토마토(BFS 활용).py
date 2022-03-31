"""
1이 있는 위치와 0이 있는 위치를 모두 저장 한다.
while이 끝난 후 0위치에 있는 것들이 모두 0이 아니라면 토마토가 모두 익은 상태다.
"""
import collections
import sys
input = lambda : sys.stdin.readline()
cols,rows = map(int,input().split())
matrix = []*rows
board = [[0]*cols for i in range(rows)]
q = collections.deque()
lst = []
move = [(1,0),(-1,0),(0,1),(0,-1)]
answer = -1
for i in range(rows):
    V = list(map(int,input().split()))
    matrix.append(V)
    for num,F in enumerate(V):
        if F==1:
            q.append([i,num])
        elif F==0:
            lst.append([i,num])

def BFS():
    while q:
        x,y = q.popleft()
        for i in move:
            if 0 <= x+i[0] < rows and 0<= y+i[1] < cols and matrix[x+i[0]][y+i[1]] ==0:
                matrix[x+i[0]][y+i[1]]=1
                board[x+i[0]][y+i[1]] = board[x][y] +1
                q.append([x+i[0],y+i[1]])
BFS()
flag = True
for r in range(rows):
    for c in range(cols):
        if matrix[r][c]==0:
            flag=False
if flag:
    for r in range(rows):
        for c in range(cols):
            answer = max(answer,board[r][c])
else:
    answer = -1
print(answer)
