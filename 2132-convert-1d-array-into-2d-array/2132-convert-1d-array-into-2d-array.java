class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
        // check
        int N = original.length;
        if (m * n != N) return new int[0][];
        
        int[][] res = new int[m][n];
        int cnt = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                res[r][c] = original[cnt++];
            }
        }
        return res;
    }
}