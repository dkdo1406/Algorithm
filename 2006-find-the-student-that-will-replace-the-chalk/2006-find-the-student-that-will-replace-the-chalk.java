class Solution {
    public int chalkReplacer(int[] chalk, int k) {
        // 100,000 * 100,000
        // 처음 10만개들 돌고 총합이 몇인지 확인한다.
        Long sum = 0L;
        for (int val : chalk) {
            sum += val;
        }
        k %= sum;
        System.out.println(k + " " + sum + " " + chalk.length);
        // 그리고 k - idx한다.
        for (int idx = 0; idx < chalk.length; idx++) {
            k -= chalk[idx];
            if (k < 0) return idx;
        }
        return 0;
    }
}