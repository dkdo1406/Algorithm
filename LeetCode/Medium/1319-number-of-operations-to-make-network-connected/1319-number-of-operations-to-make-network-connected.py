class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        check = set()
        for i, j in connections:
            check.add(i)
            check.add(j)
        
        if len(connections) == n - 1:
            return n - len(check)
        
        else:
            graph = [[] for _ in range(n)]
            for i, j in connections:
                graph[i].append(j)
                graph[j].append(i)
            q = deque()
            cnt = -1
            visit = set()
            while check or q:
                if not q:
                    temp = check.pop()
                    q.append(temp)
                    visit.add(temp)
                    cnt += 1

                start = q.popleft()
                for i in graph[start]:
                    if i in visit:
                        continue
                    q.append(i)
                    check.remove(i)
                    visit.add(i)
            return n - len(visit) + cnt



        