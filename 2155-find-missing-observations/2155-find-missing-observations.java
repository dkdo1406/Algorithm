class Solution {
    public int[] missingRolls(int[] rolls, int mean, int n) {
        int m = rolls.length;
        int isPossible = (mean * (n + m));
        for (int val : rolls) {
            isPossible -= val;
        }
        // 가능한지 확인
        if (isPossible > 6 * n || isPossible < n) return new int[0];
        int[] res = new int[n];
        for (int idx = 0; idx < n; idx++) {
            res[idx] = isPossible / (n - idx);
            isPossible -= res[idx];
        }
        
        return res;
    }
}