class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        dr = [1,-1,0,0]
        dc = [0,0,-1,1]
        n = len(grid)
        m = len(grid[0])
        q = deque()

        for R in range(n):
            for C in range(m):

                if grid[R][C] == 1 and (R == 0 or C == 0 or R == n-1 or C == m-1):
                    q.append((R, C))
                    grid[R][C] = 0
                    while q:
                        r, c = q.popleft()
                        for i in range(4):
                            nr = r + dr[i]
                            nc = c + dc[i]
                            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                                continue
                            if grid[nr][nc] == 1:
                                grid[nr][nc] = 0
                                q.append((nr, nc))
        ans = 0
        for i in grid:
            ans += sum(i)
        return ans
