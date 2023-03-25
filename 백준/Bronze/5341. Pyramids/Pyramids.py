while True:
    n = int(input())
    if n == 0:
        break
    ans = (n + 1) * (n // 2)
    if n % 2 == 1:
        ans += (n // 2) + 1
    print(ans)