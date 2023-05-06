from collections import defaultdict
from collections import deque
N = int(input())
node_set = defaultdict(set)
ans = [0] * (N + 1)

for _ in range(N-1):
    u, v = list(map(int, input().split()))
    node_set[str(u)].add(v)
    node_set[str(v)].add(u)
q = deque()
q.append(1)
while q:
    node = q.popleft()
    if str(node) in node_set:
        for n_node in node_set[str(node)]:
            ans[n_node] = node
            node_set[str(n_node)].remove(node)
            q.appendleft(n_node)

for i in range(2, N+1):
    print(ans[i])
