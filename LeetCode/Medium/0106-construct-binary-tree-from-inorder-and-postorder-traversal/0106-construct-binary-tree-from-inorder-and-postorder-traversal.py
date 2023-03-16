# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        global n
        dic = dict()
        for index, i in enumerate(inorder):
            dic[i] = index
        n = len(inorder) - 1
        tree = TreeNode()
        def dfs(node, lp, rp):
            global n
            if n < 0:
                return
            i = dic[postorder[n]]
            node.val = postorder[n]

            if i <= rp - 1:
                n -= 1
                node.right = TreeNode()
                dfs(node.right, i + 1, rp)
            
            if i >= lp + 1:
                n -= 1
                node.left = TreeNode()
                dfs(node.left, lp, i - 1)

        dfs(tree, 0, n)
        
        return tree
