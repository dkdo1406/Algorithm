class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dr = [0,0,-1,1]
        dc = [1,-1,0,0]
        q = deque()
        ans = 0
        for R in range(n):
            for C in range(m):
                if grid[R][C] == 0:
                    res = 1
                    grid[R][C] = 1
                    q.append((R, C))
                    while q:
                        r, c = q.popleft()
                        for i in range(4):
                            nr = r + dr[i]
                            nc = c + dc[i]
                            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                                res = 0
                                continue
                            if grid[nr][nc] == 0:
                                q.append((nr, nc))
                                grid[nr][nc] = 1
                    ans += res

        return ans

