n = int(input())
arr = list(map(int, input().split()))

arr_1 = []
arr_2 = []
for i in arr:
    if i == 2:
        arr_1.append(-1)
        arr_2.append(1)
    else:
        arr_1.append(1)
        arr_2.append(-1)
answer = 0
result = 0
rock = 0
for i in range(n):
    while rock < n and result >= 0:
        result += arr_1[rock]
        answer = max(answer, result)
        rock += 1
    result -= arr_1[i]
rock = 0
result = 0
for i in range(n):
    while rock < n and result >= 0:
        result += arr_2[rock]
        answer = max(answer, result)
        rock += 1
    result -= arr_2[i]
print(answer)