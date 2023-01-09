n, s = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr_sum = 0
ans = n + 1
rr = 0
for i in range(n):
    while rr < n and arr_sum < s:
        arr_sum += arr[rr]
        rr += 1
    if arr_sum >= s:
        ans = min(ans, rr - i)
    arr_sum -= arr[i]

if ans == n+1:
    print(-1)
else:
    print(ans)