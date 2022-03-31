"""
N,M 주어질 때 가장 윗줄 숫자 구하기
가장 윗줄에 1~N까지 숫자가 있다.
3 1 2 4
 4 3 6
  7 9
   16

3C0 3C1 3C2 3C3
총 4번 돌려야 하나?
"""
N,M = map(int,input().split())
lst = [i for i in range(1,N+1)]
visited = [False]*(N+1)
pm = [0]*N
answer = []
bm = [0]*N
dy = [[0]*10 for i in range(10)]
flag = False
def combi(n,r):
    if dy[n][r]!=0:
        return dy[n][r]
    if n==r or r==0:
        return 1
    else:
        dy[n][r] = combi(n-1,r-1)+combi(n-1,r)
        return dy[n][r]
for i in range(N):
    bm[i] = combi(N-1,i)


def DFS(L,sum):
    global flag
    if flag:
        return
    if L==N:
        if sum == M:
            flag = True
            for i in pm:
                print(i,end=' ')
            return
        return
    else:
        for i in lst:
            if not visited[i]:
                visited[i]=True
                pm[L]=i
                DFS(L+1,sum+(pm[L]*bm[L]))
                visited[i]=False
DFS(0,0)
