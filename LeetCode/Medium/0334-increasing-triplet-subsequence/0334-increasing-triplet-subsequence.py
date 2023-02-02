import bisect
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp = []
        dp.append(nums[0])
        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                if len(dp) == 3:
                    return True
            else:
                index = bisect.bisect_left(dp, nums[i])
                if dp[index] != nums[i]:
                    dp[index] = nums[i]
        return False