class Solution {
    public int[] applyOperations(int[] nums) {
        int[] ans = new int[nums.length];
        
        for(int idx = 0; idx < nums.length - 1; idx++) {
            if (nums[idx] == nums[idx + 1]) {
                nums[idx] = nums[idx] * 2;
                nums[idx + 1] = 0;
            }
        }
        int p = 0;
        for (int num : nums) {
            if (num == 0) continue;
            ans[p++] = num;
        }

        return ans;
    }
}