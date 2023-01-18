n = int(input())

for _ in range(n):
    num = int(input())
    temp = []
    temp.append([1, 0])
    temp.append([0, 1])
    for i in range(num):
        temp.append([0,0])
    for i in range(2, num+1):
        temp[i][0] = temp[i-1][0] + temp[i-2][0]
        temp[i][1] = temp[i-1][1] + temp[i-2][1]
    print(temp[num][0], temp[num][1])

