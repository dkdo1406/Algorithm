import sys
import heapq
input = lambda: sys.stdin.readline()
n = int(input())
classroom = []
room = []
for _ in range(n):
    i, j = list(map(int, input().split()))
    classroom.append((i, j))
    # heapq.heappush(room, (j, i))
    # classroom.append(list(map(int, input().split())))
classroom.sort(key=lambda x: x[0])
# end, start = heapq.heappop(room)
for i, j in classroom:
    if not room:
        heapq.heappush(room, j)
    else:
        end = heapq.heappop(room)
        if end > i:
            heapq.heappush(room, end)
        heapq.heappush(room, j)

print(len(room))