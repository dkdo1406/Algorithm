class Solution {
    public int[] missingRolls(int[] rolls, int mean, int n) {
        int m = rolls.length;
        int sum = 0;
        for (int val : rolls) {
            sum += val;
        }
        // 가능한지 확인
        System.out.println(m + " " + n + " " + sum);
        int isPossible = (mean * (n + m)) - sum;
        if (isPossible > 6 * n || isPossible / n == 0 || isPossible <= 0) return new int[0];
        int[] res = new int[n];
        for (int idx = 0; idx < n; idx++) {
            res[idx] = isPossible / (n - idx);
            isPossible -= res[idx];
        }
        
        return res;
    }
}