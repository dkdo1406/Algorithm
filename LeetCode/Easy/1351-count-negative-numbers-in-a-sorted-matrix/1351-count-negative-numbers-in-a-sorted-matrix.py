class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid) - 1, 0
        ans = 0
        while m >= 0 and n < len(grid[0]):
            if grid[m][n] >= 0:
                n += 1
            else:
                ans += len(grid[0]) - n
                m -= 1
        return ans        