N = int(input())
arr = list(str(N))
if N - 9 * len(arr) <= 0:
    start = 0
else:
    start = N - 9 * len(arr)

ans = 0
for i in range(start, N):
    arr = list(str(i))
    res = i
    for j in arr:
        res += int(j)
    if res == N:
        ans = i
    if ans != 0:
        break
print(ans)
