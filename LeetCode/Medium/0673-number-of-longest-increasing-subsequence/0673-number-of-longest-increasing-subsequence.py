class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        max_len = 0
        len_1 = [1] * n
        cnt = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if len_1[i] == len_1[j] + 1:
                        cnt[i] += cnt[j]
                    elif len_1[i] < len_1[j] + 1:
                        len_1[i] = len_1[j] + 1
                        cnt[i] = cnt[j]
            if max_len == len_1[i]:
                res += cnt[i]
            elif max_len < len_1[i]:
                max_len = len_1[i]
                res = cnt[i]
        return res