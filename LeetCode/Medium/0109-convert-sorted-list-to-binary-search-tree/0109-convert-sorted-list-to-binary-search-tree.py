# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        def dfs(lp, rp, tree):
            cp = (lp + rp) // 2
            tree.val = arr[cp]
            if lp < cp:
                tree.left = TreeNode()
                dfs(lp, cp, tree.left)
            if rp > cp+1:
                tree.right = TreeNode()
                dfs(cp+1, rp, tree.right)
        if arr:
            tree = TreeNode()
            dfs(0, len(arr), tree)
            return tree
        
        