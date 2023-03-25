n = int(input())
m = int(input())
if n == m:
    print(n)
    print(0)
else:
    a = n // 2
    if m % 2 == 1:
        m = (m + 1) // 2
    else:
        m //= 2
    a += m
    print(a)
    print(n - a)