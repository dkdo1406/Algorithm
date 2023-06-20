class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        radius = 2 * k + 1
        ans = [-1] * n
        if radius > n:
            return ans
        start, end, res = 0, 0, 0
        for _ in range(radius):
            res += nums[end]
            end += 1
        ans[k] = res // radius
        res -= nums[start]
        
        for i in range(k + 1, n - k):
            start += 1
            res += nums[end]
            ans[i] = res // radius
            res -= nums[start]
            end += 1

        return ans