class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        prime = []
        for i in range(len(str2), 0, -1):
            if len(str2) % i == 0 and len(str1) % i == 0:
                flag = True
                for j in range(0, len(str2), i):
                    if str2[j:j+i] != str2[:i]:
                        flag = False
                        break
                if flag:
                    prime.append(str2[:i])
        for split in prime:
            flag = True
            for i in range(0, len(str1), len(split)):
                if str1[i:i+len(split)] != split:
                    flag = False
                    break
            if flag:
                return split
        return ""
            