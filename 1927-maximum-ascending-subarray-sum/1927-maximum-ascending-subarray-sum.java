class Solution {
    public int maxAscendingSum(int[] nums) {
        int ans = nums[0];
        int temp = nums[0];
        for (int idx = 1; idx < nums.length; idx++) {
            if (nums[idx - 1] < nums[idx]) {
                temp += nums[idx];
            } else {
                temp = nums[idx];
            }
            ans = Math.max(ans, temp);
        }
        return ans;
    }
}