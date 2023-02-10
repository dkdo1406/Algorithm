import copy
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dr = [0,0,1,-1]
        dc = [1,-1,0,0]
        ans = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    continue
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if nr < 0 or nr >= N or nc < 0 or nc >= N or grid[nr][nc] == 0:
                        continue
                    if grid[r][c] == 0:
                        grid[r][c] = grid[nr][nc] + 1
                    else:
                        grid[r][c] = min(grid[r][c], grid[nr][nc] + 1)

        for r in range(N-1, -1, -1):
            for c in range(N-1, -1, -1):
                if grid[r][c] == 1:
                    continue
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if nr < 0 or nr >= N or nc < 0 or nc >= N or grid[nr][nc] == 0:
                        continue
                    if grid[r][c] == 0:
                        grid[r][c] = grid[nr][nc] + 1
                    else:
                        grid[r][c] = min(grid[r][c], grid[nr][nc] + 1)
        for i in grid:
            ans = max(ans, max(i))
        if ans < 2:
            return -1
        else:
            return ans - 1
        


