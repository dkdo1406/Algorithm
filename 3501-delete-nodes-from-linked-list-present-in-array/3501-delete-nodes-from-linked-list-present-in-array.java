/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode modifiedList(int[] nums, ListNode head) {
        
        // delete list
        Set<Integer> deleteList = new HashSet<Integer>();

        for(int num : nums) {
            deleteList.add(num);
        }
        
        // check head
        while(head != null && deleteList.contains(head.val)) {
            head = head.next;
        }
        // next
        ListNode pastNode = head;
        ListNode currentNode = pastNode.next;
        while(currentNode != null) {
            // 1. check val
            if (deleteList.contains(currentNode.val)) {
                // save node
                pastNode.next = currentNode.next;
            } else {
                pastNode = pastNode.next;
            }
            currentNode = currentNode.next;
        }


        return head;

    }
}