n = int(input())
arr = [input() for _ in range(n)]
answer = []
for i in range(len(arr[0])):
    temp = arr[0][i]
    answer.append(temp)
    for j in arr:
        if temp != j[i]:
            answer[-1] = "?"
            break
print(''.join(answer))
