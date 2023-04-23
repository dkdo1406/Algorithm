import sys
input = lambda : sys.stdin.readline()

N = int(input())
arr = list(map(int, input().split()))
operatior = list(map(int, input().split()))

min_val = 10 ** 9
max_val = -10 ** 9

def dfs(i, oper, num):
    global min_val, max_val
    if i == N:
        min_val = min(min_val, num)
        max_val = max(max_val, num)
        return
    if oper[0] > 0:
        oper[0] -= 1
        dfs(i + 1, oper, num + arr[i])
        oper[0] += 1
    if oper[1] > 0:
        oper[1] -= 1
        dfs(i + 1, oper, num - arr[i])
        oper[1] += 1
    if oper[2] > 0:
        oper[2] -= 1
        dfs(i + 1, oper, num * arr[i])
        oper[2] += 1
    if oper[3] > 0:
        oper[3] -= 1
        if num < 0 or arr[i] < 0:
            dfs(i + 1, oper, -(abs(num) // abs(arr[i])))
        else:
            dfs(i + 1, oper, (abs(num) // abs(arr[i])))
        oper[3] += 1

dfs(1, operatior, arr[0])
print(max_val)
print(min_val)