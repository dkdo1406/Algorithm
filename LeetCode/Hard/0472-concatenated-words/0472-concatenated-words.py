class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def dfs(prefix):
            for i in range(1, len(prefix)):
                if prefix[:i] in vocab:
                    suffix = prefix[i:]
                    if suffix in vocab or dfs(suffix):
                        return True
            return False

        vocab = set(words)
        res = []
        for i in words:
            if dfs(i):
                res.append(i)
        return res