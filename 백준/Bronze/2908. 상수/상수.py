N, M = list(map(int, input().split()))

new_n = ''.join(list(reversed(str(N))))
new_m = ''.join(list(reversed(str(M))))
print(max(new_n, new_m))