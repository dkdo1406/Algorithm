n = int(input())
arr = list(map(int, input().split()))
rr = 0
sum_arr = 0
dic = dict()
answer = 0
for i in range(n):
    while rr < n and arr[rr] not in dic:
        sum_arr += arr[rr]
        dic[arr[rr]] = 1
        rr += 1
    answer = max(answer, len(dic))
    sum_arr -= arr[i]
    dic.pop(arr[i])
print(answer)