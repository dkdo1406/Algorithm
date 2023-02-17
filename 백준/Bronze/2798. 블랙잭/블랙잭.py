N, M = list(map(int, input().split()))
cards = list(map(int, input().split()))
cards.sort()

ans = cards[0] + cards[1] + cards[2]
for i in range(N-2):
    l = r = i
    l += 1
    r += 2
    black = cards[i] + cards[l] + cards[r]
    while l < N-1:
        black = cards[i] + cards[l] + cards[r]
        if M < black:
            if r - l == 1:
                break
            l += 1
            r = l
            r += 1
        elif M == black:
            ans = M
            break
        elif M > black:
            ans = max(ans, black)
            if r == N-1:
                l += 1
            else:
                r += 1
    if ans == M:
        break
print(ans)
