class Solution {
    public int maxAbsoluteSum(int[] nums) {
        int ans = Math.abs(nums[0]);
        int[] max = new int[nums.length];
        int[] min = new int[nums.length];
        max[0] = nums[0];
        min[0] = nums[0];
        int temp;
        for (int idx = 1; idx < nums.length; idx++) {
            max[idx] = Math.max(nums[idx], nums[idx] + max[idx - 1]);
            min[idx] = Math.min(nums[idx], nums[idx] + min[idx - 1]);
            temp = Math.max(Math.abs(min[idx]), max[idx]);
            ans = Math.max(ans, temp);
        }
        
        return ans;
    }
}