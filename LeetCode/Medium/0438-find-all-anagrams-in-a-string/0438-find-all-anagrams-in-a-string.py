from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic = defaultdict(int)
        check_dic = defaultdict(int)
        ans = []
        if len(s) < len(p):
            return []
        for i in p:
            dic[i] += 1
        for i in range(len(p)):
            check_dic[s[i]] += 1
        if check_dic == dic:
            ans.append(0)
        for i in range(len(s)-len(p)):
            check_dic[s[i]] -= 1
            check_dic[s[i+len(p)]] += 1
            if check_dic[s[i]] == 0:
                check_dic.pop(s[i])
            if check_dic == dic:
                ans.append(i+1)
        return ans