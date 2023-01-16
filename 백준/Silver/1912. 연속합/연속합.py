n = int(input())
arr = list(map(int, input().split()))

answer = -1000000000
check = 0
result = 0
for i in range(n):
    while check < n and result >= 0:
        result += arr[check]
        check += 1
        answer = max(answer, result)

    result -= arr[i]
print(answer)