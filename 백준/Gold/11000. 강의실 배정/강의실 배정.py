import sys
import heapq
input = lambda: sys.stdin.readline()
n = int(input())
classroom = []
room = []
for _ in range(n):
    i, j = list(map(int, input().split()))
    classroom.append((i, j))

classroom.sort(key=lambda x: x[0])
for i, j in classroom:
    if not room:
        heapq.heappush(room, j)
    else:
        end = heapq.heappop(room)
        if end > i:
            heapq.heappush(room, end)
        heapq.heappush(room, j)

print(len(room))