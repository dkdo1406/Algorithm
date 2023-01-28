class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                if word == s[i - len(word) + 1 : i + 1] and (d[i - len(word)] or i - len(word) + 1 == 0):
                    d[i] = True
        return d[-1]