class Solution {
    public int minSteps(int n) {
        int[] dp = new int[n + 1];
        // copy 1로만 했을 때
        dp[1] = 0;
        for (int idx = 2; idx < n + 1; idx++) {
            dp[idx] = idx;
        }
        // copy or paste

        for (int idx = 2; idx <= n / 2; idx++) {
            // 현재 값에서 copy
            for (int cnt = 2; cnt <= n / idx; cnt++) {
                dp[idx * cnt] = Math.min(dp[idx * cnt], dp[idx] + cnt);
            }
        }
        return dp[n];
    }
}