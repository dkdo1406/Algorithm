class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        if n == maxSum:
            return 1
        if n == 1:
            return maxSum
        l_c, r_c = index, n - index - 1
        left, right, ans = 2, maxSum - n, 0
        while left <= right:
            mid = (left + right) // 2
            if self.conditions(l_c, r_c, n, index, maxSum - mid, mid - 1):
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
        return ans
    
    def conditions(self, left_cnt, right_cnt, n, index, maxSum, c):
        res = 0
        if left_cnt >= c - 1:
            res += left_cnt - (c - 1)
            res += (c + 2) * ((c - 1) // 2)
            if (c - 1) % 2 == 1:
                res += (c + 2) // 2
        else:
            res += (c + c - (left_cnt - 1)) * (left_cnt // 2)
            if left_cnt % 2 == 1:
                res += (c + c - (left_cnt - 1)) // 2

        if right_cnt >= c - 1:
            res += right_cnt - (c - 1)
            res += (c + 2) * ((c - 1) // 2)
            if (c - 1) % 2 == 1:
                res += (c + 2) // 2
        else:
            res += (c + c - (right_cnt - 1)) * (right_cnt // 2)
            if right_cnt % 2 == 1:
                res += (c + c - (right_cnt - 1)) // 2

        return res <= maxSum