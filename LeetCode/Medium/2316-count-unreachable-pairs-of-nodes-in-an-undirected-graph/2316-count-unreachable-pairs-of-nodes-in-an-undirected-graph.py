class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        graph = [[] for _ in range(n)]
        check = set()
        visit = set()

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
            check.add(i)
            check.add(j)
        
        q = deque()
        cnt = 0
        ans = 0
        total = []
        while q or check:
            if not q:
                if cnt != 0:
                    total.append(cnt)
                tmp = check.pop()
                q.append(tmp)
                visit.add(tmp)
                cnt = 1

            s = q.popleft()

            for i in graph[s]:
                if i in visit:
                    continue
                q.append(i)
                visit.add(i)
                check.remove(i)
                cnt += 1
        if cnt != 0:
            total.append(cnt)
        if total:
            for i in total:
                n -= i
                ans += i * n
        n -= 1
        
        ans += (n + 1) * (n // 2)
        if n % 2 == 1:
            ans += (n // 2) + 1

        return ans


            