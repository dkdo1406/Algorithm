n = int(input())
lst = list(map(int,input().split()))
module = list(map(int,input().split()))

def dfs(cnt, result, p, m, mul, d):
    global max_result, min_result
    if cnt == n:
        max_result = max(result, max_result)
        min_result = min(result, min_result)
    if p:
        dfs(cnt+1, result + lst[cnt], p - 1, m, mul, d)
    if m:
        dfs(cnt + 1, result - lst[cnt], p, m - 1, mul, d)
    if mul:
        dfs(cnt + 1, result * lst[cnt], p, m, mul - 1, d)
    if d:
        dfs(cnt + 1, -(-result // lst[cnt]) if result < 0 else result // lst[cnt], p, m, mul, d - 1 )

result = 0
max_result = -100000001
min_result = 1000000001
dfs(1, lst[0], module[0], module[1], module[2], module[3])
print(max_result)
print(min_result)