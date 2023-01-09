A,B,N = list(map(int, input().split()))

cnt = 0
result = 0
while cnt < N:
    if A // B == 0:
        result = (A * 10) // B
        A = (A * 10) % B
        cnt += 1
    else:
        result = A // B
        A = A % B
print(result)