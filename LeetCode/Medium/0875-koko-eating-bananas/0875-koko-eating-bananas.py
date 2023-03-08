class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        lp = 1
        rp = max(piles)
        while lp < rp:
            time = 0
            cp = (lp + rp) // 2
            for i in range(n):
                if piles[i] % cp == 0:
                    time += piles[i] // cp
                else:
                    time += piles[i] // cp + 1
            if time > h:
                lp = cp + 1
            else:
                rp = cp
        return lp