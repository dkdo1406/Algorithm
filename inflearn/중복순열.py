"""
1부터 N까지 적힌 구슬이 있다.
중복허락하여 M개를 뽑아 나열하는 경우를 모두 출력하라.
1부터시작하여 L이 N이 되면 return하게 한다.
"""
N,M = map(int,input().split())
pm = [0]*(N-1)
def DFS(L):
    if L==M:
        for i in pm:
            print(i,end=' ')
        print()
        return
    else:
        for i in range(1,N+1):
            pm[L]=i
            DFS(L+1)
DFS(0)