n, m = list(map(int, input().split()))
arrN = list(map(int, input().split()))
arrM = list(map(int, input().split()))

lr = 0
answer = "Yes"
for i in arrM:
    while lr < n-1 and arrN[lr] != i:
        lr += 1
    if arrN[lr] != i:
        answer = "NO"
print(answer)
