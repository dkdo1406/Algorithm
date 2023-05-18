import heapq

m, n = list(map(int, input().split()))
cards = list(map(int, input().split()))
heapq.heapify(cards)

for _ in range(n):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    heapq.heappush(cards, a+b)
    heapq.heappush(cards, a + b)

print(sum(cards))