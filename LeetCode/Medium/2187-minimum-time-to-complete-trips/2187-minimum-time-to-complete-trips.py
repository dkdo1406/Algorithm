class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        pl = 0
        pr = totalTrips * min(time)
        ans = 10e15
        while pl <= pr:
            pc = (pl + pr) // 2
            total = 0
            for i in time:
                total += pc // i
            if totalTrips > total:
                pl = pc + 1
            else:
                pr = pc - 1
                ans = min(ans, pc)
        return ans
                

