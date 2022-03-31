"""
0은 빈칸, 1은 집, 2는 피자집
각 집마다 피자배달거리가 있는데 |x1-x2|+|y1-y2|이다.
N*N 도시, M개의 피자집
피자배달거리가 최소가 되는 M개의 피자집만 선택할 때 도시의 최소피자배달거리는?
4 4
0 1 2 0
1 0 2 1
0 2 1 2
2 0 1 2

"""
N,M = list(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]
house = [] #집좌표
pz = [] #피자좌표
combi = [0]*N #nCr 순서저장
answer = (N+N)*M
for i in range(N):
    for j in range(N):
        if board[i][j]==1:
            house.append([i,j])
        elif board[i][j]==2:
            pz.append([i,j])
pz_len = len(pz)
def DFS(L,s): #피자 순서 저장
    global answer
    if(L==M): # 모든 피자 조합 나왔음
        sum =0
        for i in house:
            dis = (N+N)*M
            for j in combi:
                dis = min(dis, abs(i[0]-pz[j][0])+abs(i[1]-pz[j][1])) #피자배달거리 최소값
            sum +=dis

        answer = min(answer,sum)
    else:
        for i in range(s,pz_len):
            combi[L]=i
            DFS(L+1,i+1)

DFS(0,0)
print(answer)

