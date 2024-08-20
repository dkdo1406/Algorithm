class Solution {
    public int stoneGameII(int[] piles) {
        if (piles.length == 0) return 0;
        int n = piles.length;
        int[][] dp = new int[n][n+1];
        int[] suffixSum = new int[n];
        suffixSum[n - 1] = piles[n - 1];
        for (int idx = n - 2; idx >= 0; idx--) {
            suffixSum[idx] = suffixSum[idx + 1] + piles[idx];
        }
        for (int idx = n - 1; idx >= 0; idx--) { // 뒤에서 부터 확인
            for (int m = 1; m <= n; m++) { // 파이프 길이는 전체 길이보다 짧아야 한다.
                if ( idx + 2 * m >= n) { // 남은 돌을 다 가져갈 수 있다면 모두 가져감
                    dp[idx][m] = suffixSum[idx];
                } else { // 평범한 상황. x는 1<= x <= 2 * m임.
                    for (int x = 1; x <= 2 * m; x++) {
                        // 현재 idx의 
                        dp[idx][m] = Math.max(dp[idx][m], suffixSum[idx] - dp[idx + x][Math.max(m, x)]);
                    }
                }
            }
        }
        return dp[0][1];
    }
}