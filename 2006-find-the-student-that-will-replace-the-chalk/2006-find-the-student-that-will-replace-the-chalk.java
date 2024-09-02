class Solution {
    public int chalkReplacer(int[] chalk, int k) {
        // 처음 총합이 몇인지 확인한다.
        Long sum = 0L;
        for (int val : chalk) {
            sum += val;
        }
        k %= sum;
        // 그리고 k - idx한다.
        for (int idx = 0; idx < chalk.length; idx++) {
            k -= chalk[idx];
            if (k < 0) return idx;
        }
        return 0;
    }
}