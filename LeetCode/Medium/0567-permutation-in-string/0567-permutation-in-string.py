from collections import defaultdict
import copy
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        dic = defaultdict(int)
        check_dic = defaultdict(int)
        for i in s1:
            dic[i] += 1
        for i in range(len(s1)):
            check_dic[s2[i]] += 1
        if check_dic == dic:
            return True
        for i in range(len(s2)-len(s1)):
            check_dic[s2[i]] -= 1
            check_dic[s2[i+len(s1)]] += 1
            if check_dic[s2[i]] == 0:
                check_dic.pop(s2[i])
            if check_dic == dic:
                return True
        return False