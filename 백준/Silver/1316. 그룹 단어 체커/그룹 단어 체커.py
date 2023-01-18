n = int(input())

answer = 0
for _ in range(n):
    arr = input()
    dic = dict()
    for i in range(len(arr)):
        if arr[i] not in dic:
            dic[arr[i]] = 1
        else:
            if arr[i-1] != arr[i]:
                answer -= 1
                break
    answer += 1
print(answer)