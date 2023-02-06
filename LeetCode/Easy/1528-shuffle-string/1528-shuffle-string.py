class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = [""] * len(indices)
        for index, i in enumerate(indices):
            arr[i] = s[index]
        ans = ''.join(arr)
        return ans