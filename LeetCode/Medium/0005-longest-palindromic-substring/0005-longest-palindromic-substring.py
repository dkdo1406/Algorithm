class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            for j in range(len(s), i-1, -1):        
                if j - i + 1 < len(ans):
                    break
                if s[i] == s[j-1] and s[i:j] == ''.join(reversed(s[i:j])):
                    if j - i + 1 > len(ans):
                        ans = s[i:j]
        return ans
