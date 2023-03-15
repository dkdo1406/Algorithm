class Solution:
    def trap(self, height: List[int]) -> int:
        max_height = 0
        n = len(height)
        dp = []
        for i in range(n):
            h = height[i]
            max_height = max(max_height, h)
            dp.append(max_height - h)
        rev_dp = []
        max_height = 0
        for i in range(n-1, -1, -1):
            h = height[i]
            max_height = max(max_height, h)
            rev_dp.append(max_height - h)
        rev_dp.reverse()
        ans = 0
        for i in range(n):
            ans += min(dp[i], rev_dp[i])
        return ans
        