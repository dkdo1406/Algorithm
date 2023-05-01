class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        alice = DSU(n+1)
        bob = DSU(n+1)
        edges.sort(key=lambda x : -x[0])
        for t, u, v in edges:
            if t == 1:
                ans += alice.union(u, v)
            elif t == 2:
                ans += bob.union(u, v)
            else:
                ans += alice.union(u, v)
                bob.union(u, v)
        tmp = alice.find(1)
        for i in range(1, n+1):
            if alice.find(i) != bob.find(i) or tmp != alice.find(i):
                return -1

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
            return 1
        if self.size[u] > self.size[v]:
            self.parent[v] = u
            self.size[u] += self.size[v]
        else:
            self.parent[u] = v
            self.size[v] += self.size[u]
        return 0