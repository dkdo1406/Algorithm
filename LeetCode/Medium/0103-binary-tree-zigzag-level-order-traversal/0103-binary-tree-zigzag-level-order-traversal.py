# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        global ans
        ans = []
        def bfs(root):
            global ans
            if root == None:
                return
            deq = deque()
            q = deque()
            ans.append([root.val])
            if root.right != None:
                deq.append([1, root.right])
            if root.left != None:
                deq.append([1, root.left])
            while deq or q:
                while deq:
                    L, root = deq.popleft()
                    if root == None:
                        continue
                    if len(ans) == L:
                        ans.append([root.val])
                    else:
                        ans[L].append(root.val)
                    if L % 2 != 0:
                        q.appendleft((L+1, root.right))
                        q.appendleft((L+1, root.left))
                    else:
                        q.appendleft((L+1, root.left))
                        q.appendleft((L+1, root.right))
                while q:
                    L, root = q.popleft()
                    if root == None:
                        continue
                    if len(ans) == L:
                        ans.append([root.val])
                    else:
                        ans[L].append(root.val)
                    if L % 2 != 0:
                        deq.appendleft((L+1, root.right))
                        deq.appendleft((L+1, root.left))
                    else:
                        deq.appendleft((L+1, root.left))
                        deq.appendleft((L+1, root.right))
            return ans
        bfs(root)
        return ans