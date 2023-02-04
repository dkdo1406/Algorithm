from collections import deque
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for i in range(n)]
        for s, d, c in flights:
            graph[s].append([d, c])
        q = deque()
        q.append([graph[src], 0, k])
        visited_cost = defaultdict(int)
        visited_cost[dst] = -1
        while q:
            yep,cost, k = q.popleft()
            for d, c in yep:
                if d == dst:
                    if visited_cost[dst] == -1:
                        visited_cost[dst] = cost + c
                    else:
                        visited_cost[dst] = min(visited_cost[dst], cost + c)
                else:
                    if k == 0:
                        continue
                    else:
                        if d not in visited_cost:
                            visited_cost[d] = cost + c
                            q.append([graph[d], cost + c, k - 1])
                        elif d in visited_cost and visited_cost[d] > cost + c:
                            visited_cost[d] = cost + c
                            q.append([graph[d], cost + c, k - 1])

        return visited_cost[dst]