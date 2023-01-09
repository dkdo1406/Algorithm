n, a, b = list(map(int, input().split()))
arr = list(map(int, input().split()))

rr = 0
arr_sum = 0
answer = n + 1
for i in range(n):
    while rr < n and arr_sum < a:
        arr_sum += arr[rr]
        rr += 1

    if arr_sum >= a and arr_sum <= b and rr - i != 1:
        print("answer", arr_sum, i, rr)
        answer = min(answer, rr - i)
    arr_sum -= arr[i]


if answer == n + 1:
    print(-1)
else:
    print(answer)
