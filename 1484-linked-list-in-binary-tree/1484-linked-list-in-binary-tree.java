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
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    static boolean ans;
    static ListNode origin;
    static Set<TreeNode> visited;
    public boolean isSubPath(ListNode head, TreeNode root) {
        ans = false;
        // 주어진 head 경로로 이루어진 노드가 있는가?
        origin = head;
        visited = new HashSet<TreeNode>();
        // Dfs

        visited.add(root);
        DFS(head, root);

        return ans;
    }
    void DFS(ListNode head, TreeNode root) {
        // ans 인지 확인
        if (ans || root == null || head == null) return;
        
        
        // 현재 head와 같은지 확인
        if (head.val == root.val) {
            if (head.next == null) {
                ans = true;
                return;
            }
            DFS(head.next, root.left);
            DFS(head.next, root.right);
            
        } else {
            // 다르더라도 밑으로 내려가 다음 노드가 같은지 확인은 해야함
            DFS(origin, root.left);
            DFS(origin, root.right);
        }

        // 처음 head와 같은지 확인 하지만 처음 가는 노드가 아니라면 다시 할 필요는 없음
        if (!visited.contains(root)) {
            visited.add(root);
            DFS(origin, root);
        }
    }

    public class Point {
        private TreeNode node;

        public Point(TreeNode node) {
            this.node = node;
        }

        @Override
        public boolean equals(Object o) {
            if(this == o) return true;
            if (!(o instanceof Point)) return false;
            Point point = (Point)o;
            return node.left == point.node.left && Objects.equals(node.right, point.node.right);
        }

        @Override
        public int hashCode() {
            return Objects.hashCode(node);
        }
    }
    
}