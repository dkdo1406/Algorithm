class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        graph = [[0 for _ in range(n)] for _ in range(m)]
        graph[0][0] = grid[0][0]
        for i in range(1, m):
            graph[i][0] = graph[i-1][0] + grid[i][0]
        for i in range(1, n):
            graph[0][i] = graph[0][i-1] + grid[0][i]
        
        for r in range(1, m):
            for c in range(1, n):
                graph[r][c] = min(graph[r-1][c],graph[r][c-1]) + grid[r][c]

        return graph[m-1][n-1]