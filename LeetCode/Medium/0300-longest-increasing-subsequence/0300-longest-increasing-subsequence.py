import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])
        for i in range(1,len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
            else:
                index = bisect.bisect_left(dp, nums[i])
                if dp[index] != nums[i]:
                    dp[index] = nums[i]
        return len(dp)
            
