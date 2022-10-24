from collections import deque
F,S,G,U,D = list(map(int, input().split()))

# F : 총 길이, S : 현재 G: 목적지, U: 위로 D: 아래로
current = S
dep = G
result = 100000000000
visited = [False] * (F+1)
def goInterview():
    global result
    q = deque()
    q.append((current,0))
    visited[S] = True
    while q:
        curr, cnt = q.popleft()
        if curr == G:
            result = cnt
            break
        if cnt > result or curr > F or curr < 1:
            continue
        if curr + U <= F and not visited[curr + U]:
            q.append((curr+U, cnt+1))
            visited[curr+U] = True
        if curr - D > 0 and not visited[curr - D]:
            q.append((curr-D, cnt+1))
            visited[curr - D] = True
goInterview()
if result == 100000000000:
    print("use the stairs")
else:
    print(result)