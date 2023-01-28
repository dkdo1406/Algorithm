class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [[-1] for _ in range(len(s))]
        
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i - len(w) + 1:i + 1] and (dp[i - len(w)] != [-1] or i - len(w) + 1 == 0):
                    if dp[i] == [-1]:
                        dp[i] = [i - len(w) + 1]
                    else:
                        dp[i].append(i - len(w) + 1)
        
        for i in range(len(dp)):
            dp[i] = sorted(dp[i], reverse = True)

        answer = []
        def check(arr, L, word):
            for i in arr:
                if i == -1:
                    return
                if i == 0:
                    if L == len(s):
                        word = s[i:L]
                    else:
                        word = s[i:L] + " " + word
                    answer.append(word)
                    return
                if L == len(s):
                    check(dp[i-1], i, s[i:L])
                else:
                    check(dp[i-1], i, s[i:L] + " " + word)
        check(dp[-1], len(s), "")
        
        return answer


