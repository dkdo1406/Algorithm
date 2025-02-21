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
class FindElements {
    private static Set<Integer> elements;
    public FindElements(TreeNode root) {
        elements = new HashSet<>();
        elements.add(0);
        check(root, 0);
    }
    
    public boolean find(int target) {
        return elements.contains(target);
    }

    public void check(TreeNode root, int val) {
        if (root.left != null) {
            elements.add(2 * val + 1);
            check(root.left, 2 * val + 1);
        }
        if (root.right != null) {
            elements.add(2 * val + 2);
            check(root.right, 2 * val + 2);
        }
    }
}

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements obj = new FindElements(root);
 * boolean param_1 = obj.find(target);
 */