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
    static int[][]graph;
    static int[] dr = {0, 1, 0, -1};
    static int[] dc = {1, 0, -1, 0};
    static int r = 0;
    static int c = 0;
    static int dir;
    static int cnt;
    public int[][] spiralMatrix(int m, int n, ListNode head) {
        graph = new int[m][n];
        dir = 0;
        r = 0;
        c = 0;
        int R = 1;
        int C = 0;
        cnt = 0;

        while (cnt < m * n) {
            if (dir % 2 == 0) {
                for (int idx = C; idx < n; idx++) {
                    head = checkHead(dir, head, m, n);
                }
                C += 1;
            } else {
                for (int idx = R; idx < m; idx++) {
                    head = checkHead(dir, head, m, n);
                }
                R += 1;
            }
            r -= dr[dir];
            c -= dc[dir];
            dir += 1;
            dir %= 4;
            r += dr[dir];
            c += dc[dir];
        }
        
        return graph;
    }

    ListNode checkHead(int dir, ListNode head, int R, int C) {
        int nr, nc;
        cnt += 1;
        
        if (head == null) {
            graph[r][c] = -1;
        } else {
            graph[r][c] = head.val;
            head = head.next;
        }
        r += dr[dir];
        c += dc[dir];
        
        // r = nr;
        // c = nc;
        return head;
    }

}