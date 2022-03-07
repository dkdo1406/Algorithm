a = int(input())
lst = map(int, input().split())
answer = 0
for i in lst:
    if i == 0 or i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            answer -= 1
            break
    answer += 1
print(answer)
