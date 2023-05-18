N, L = list(map(int, input().split()))
pipe = list(map(int, input().split()))

pipe.sort()
ans = 0
tape = 0
for i in pipe:
    if tape < i:
        ans += 1
        tape = i + L - 1
print(ans)