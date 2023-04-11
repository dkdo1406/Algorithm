class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        ans = []
        for i in spells:
            lp = 0
            rp = n
            while lp < rp:
                mid = (lp + rp) // 2
                if potions[mid] * i < success:
                    lp = mid + 1
                else:
                    rp = mid
            ans.append(n - lp)
        
        return ans
            