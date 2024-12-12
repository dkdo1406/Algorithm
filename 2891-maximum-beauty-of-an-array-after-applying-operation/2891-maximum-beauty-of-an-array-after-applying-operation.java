class Solution {
    public int maximumBeauty(int[] nums, int k) {
        int n = nums.length;
        // 처음부터 교체하는데, 값의 범위는 해당 값 - k ~ 해당값 + k까지이다.
        // 같은값으로 연속되어 있는 값이 가장 아름다운 값이다.
        // 같은값이 최대 몇개있는지 리턴하라.

       Arrays.sort(nums);
       int l, r, c, lNum, rNum, cnt;
       int ans = 0;
       for (int idx = 0; idx < n; idx++) {
        l = idx;
        r = n - 1;
        cnt = 1;
        lNum = nums[idx] + k;
        
        while (l <= r) {
            c = (l + r) / 2;
            rNum = Math.max(nums[c] - k, 0);

            if (lNum < rNum) {
                r = c - 1;
            } else {
                l = c + 1; 
            }
        }
        // 최종 r 위치
        ans = Math.max(ans, l - idx);
       }
        

        
        return ans;
    }
}