from collections import deque

N = 3

a,b = list(map(int, input().split()))
graph = [[0 for _ in range(a+1)] for _ in range(a+1)]

lst = []
for _ in range(b):
    temp = list(map(int, input().split()))
    x, y, x1, y1 = temp
    if x > y:
        x, y = y, x
    temp = x, y, x1+y1
    lst.append(temp)
print(lst)
lst.sort(key = lambda x: (x[0]))



def bfs(n, result):
    global a, lst
    visited = [False] * (a + 1)
    visited[1] = True
    q = deque()
    q.append([n, result, visited])

    minValue = 10000000001
    while q:
        new, add, newVisited = q.popleft()
        if new == 2:
            minValue = min(minValue, add)
        for idx in lst:
            if minValue < add:
                continue
            newAdd = add
            visited = []
            visited += newVisited
            if idx[0] == new and not visited[idx[1]]:
                visited[idx[1]] = True
                newAdd *= idx[2]
                q.append([idx[1], newAdd, visited])
            if idx[1] == new and not visited[idx[0]]:
                visited[idx[0]] = True
                newAdd *= idx[2]
                q.append([idx[0], newAdd, visited])
    return minValue

print(bfs(1, 1))


