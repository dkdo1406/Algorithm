N = int(input())
sum = 0

if N == 1:
    print(N)
else:
    for i in range(1, N+1):
        sum += i
    print(sum)