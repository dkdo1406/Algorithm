# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        global arr
        arr = set()
        
        def dfs(root):
            global arr
            arr.add(root.val)
            if root.left != None:
                left_root = root.left
                dfs(left_root)
            if root.right != None:
                right_root = root.right
                dfs(right_root)
        dfs(root)
        sort_arr = sorted(list(arr))
        ans = 10000000
        for i in range(1, len(sort_arr)):
            ans = min(ans, sort_arr[i] - sort_arr[i-1])
        return ans