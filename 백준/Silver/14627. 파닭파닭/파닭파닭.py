import sys
input = lambda: sys.stdin.readline()
S, C = list(map(int, input().split()))

make_c = dict()
sum_pa = 0
pa = []
for _ in range(S):
    L = int(input())
    pa.append(L)
    sum_pa += L
lp = 1
rp = 1000000000
res = 0
while lp <= rp:
    c = (lp + rp) // 2
    cnt = 0
    for i in pa:
        cnt += (i // c)
    if cnt >= C:
        lp = c + 1
        res = c
        make_c[str(res)] = cnt
    else:
        rp = c - 1
print(sum_pa - res * C)