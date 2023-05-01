class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dsu = DSU(n)
        for i in range(len(queries)):
            queries[i].append(i)
        edgeList.sort(key=lambda x : x[2])
        queries.sort(key=lambda x : x[2])
        ans = [False] * len(queries)
        index = 0
        for q in queries:
            while index < len(edgeList) and edgeList[index][2] < q[2]:
                dsu.union(edgeList[index][0], edgeList[index][1])
                index += 1
            if dsu.find(q[0]) == dsu.find(q[1]):
                ans[q[3]] = True
        
        return ans


class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return
        if self.size[u] > self.size[v]:
            self.parent[v] = u
            self.size[u] += self.size[v]
        else:
            self.parent[u] = v
            self.size[v] += self.size[u]