class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        scoreage = list(zip(scores,ages))
        scoreage.sort(key = lambda x: (x[0], x[1]))
        dp = [0] * (max(ages) + 1)
        for score, age in scoreage:
            dp[age] = score + max(dp[:age + 1])
        return max(dp)
