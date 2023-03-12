# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans_arr = []
        for node in lists:
            while node is not None:
                ans_arr.append(node.val)
                node = node.next
        ans_arr.sort()
        ans_node = ans = ListNode()
        for i in ans_arr:
            ans.next = ListNode(i)
            ans = ans.next
        return ans_node.next
        
