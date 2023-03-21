class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt = 0
        ans = 0
        dic = collections.defaultdict(int)
        for i in nums:
            if i == 0:
                cnt += 1
                continue
            if cnt != 0:
                dic[cnt] += 1
            cnt = 0
        if cnt != 0:
            dic[cnt] += 1

        for key, value in dic.items():
            res = (key + 1) * (key//2)
            if key % 2 == 1:
                res += key // 2 + 1
            ans += res * value
        
        return ans