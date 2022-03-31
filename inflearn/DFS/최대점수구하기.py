N,M = map(int,input().split())
ps,pt = [],[]
for _ in range(N):
    s,t = map(int,input().split())
    ps.append(s)
    pt.append(t)
answer = 0
def DFS(L,sum,T,ps,pt):
    global answer
    if T>M:
        return
    if L==N:
        answer = max(answer,sum)
        return
    else:
        DFS(L + 1, sum + ps[L], T + pt[L], ps, pt)  # 더하는 경우
        DFS(L + 1, sum, T, ps, pt)  # 안 더하는 경우


DFS(0,0,0,ps,pt)
print(answer)