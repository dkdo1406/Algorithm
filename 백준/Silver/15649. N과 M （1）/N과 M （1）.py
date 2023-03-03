N, M = list(map(int, input().split()))

def permu(arr ,cnt, chk):
    if cnt == M:
        for i in arr:
            print(i, end=" ")
        print()
        return
    else:
        for i in range(1, N + 1):
            if i in chk:
                continue
            else:
                chk.add(i)
                permu(arr + [i], cnt + 1, chk)
                chk.remove(i)
check = set()
permu([], 0, check)

