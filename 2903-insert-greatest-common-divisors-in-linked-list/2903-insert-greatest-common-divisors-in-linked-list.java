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
    public ListNode insertGreatestCommonDivisors(ListNode head) {
        ListNode prev = head;
        ListNode curr = prev.next;
        ListNode insert;
        while(curr != null) {
            // prev와 curr의 최대공약수 찾기
            insert = new ListNode();
            int a, b;
            if (prev.val < curr.val) {
                a = prev.val;
                b = curr.val;
            } else {
                a = curr.val;
                b = prev.val;
            }
            insert.val = GCD(a, b);
            // prev.next에 넣기
            prev.next = insert;
            insert.next = curr;
            prev = curr;
            curr = curr.next;
        }

        return head;
    }
    int GCD(int a, int b) {
            int r = a % b;
            if (r == 0) return b;

            return GCD(b, r); 
        }
}