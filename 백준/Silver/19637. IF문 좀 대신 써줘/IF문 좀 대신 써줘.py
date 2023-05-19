import sys
input = lambda : sys.stdin.readline()
N, M = list(map(int, input().split()))

strong = []
for _ in range(N):
    S, P = list(input().split())
    strong.append((S, int(P)))
ans = [0] * M
arr = []
for i in range(M):
    arr.append((int(input()), i))
arr.sort()
i = 0
for char_power, index in arr:
    if i == N:
        break
        
    while i < N:
        S, power = strong[i]
        if char_power <= power:
            ans[index] = S
            break
        else:
            i += 1

for i in ans:
    print(i)