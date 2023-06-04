import copy
import sys
input = lambda:sys.stdin.readline()
n = int(input())

tmp = list(map(int, input().split()))
max_graph = copy.deepcopy(tmp)
min_graph = copy.deepcopy(tmp)
tmp.clear()
for _ in range(1, n):
    tmp = list(map(int, input().split()))
    tmp_max_graph = copy.deepcopy(tmp)
    tmp_min_graph = copy.deepcopy(tmp)
    tmp_max_graph[0] += max(max_graph[0], max_graph[1])
    tmp_min_graph[0] += min(min_graph[0], min_graph[1])
    tmp_max_graph[1] += max(max_graph)
    tmp_min_graph[1] += min(min_graph)
    tmp_max_graph[2] += max(max_graph[1], max_graph[2])
    tmp_min_graph[2] += min(min_graph[1], min_graph[2])

    max_graph = copy.deepcopy(tmp_max_graph)
    min_graph = copy.deepcopy(tmp_min_graph)

print(max(max_graph), min(min_graph))