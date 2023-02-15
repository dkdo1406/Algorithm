class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        cnt = len(num) - 1
        number = 0
        for i in num:
            number += i * (10 ** cnt)
            cnt -= 1
        ans = number + k
        
        ans_lst = list(map(int, str(ans)))
        return ans_lst
            