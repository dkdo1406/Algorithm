class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        res = []
        ans = []
        for i in obstacles:
            if not ans or i >= ans[-1]:
                ans.append(i)
            else:
                index = bisect.bisect_right(ans, i)
                if ans[index] != i:
                    res.append(index+1)
                    ans[index] = i
                    continue

            res.append(len(ans))
        
        return res