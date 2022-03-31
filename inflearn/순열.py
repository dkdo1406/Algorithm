"""
10이하의 N자연수 중 M개를 뽑아 일렬로 나열
"""
N,M = map(int,input().split())
lst = list(map(int,input().split()))
visted = [False]*11
pm = [0]*(M)
def DFS(L,visted):
    if L==M:
        for i in pm:
            print(i,end=" ")
        print()
        return
    else:
        for i in lst:
            if not visted[i]:
                visted[i]=True
                pm[L] = i
                DFS(L+1,visted)
                visted[i]=False

DFS(0,visted)