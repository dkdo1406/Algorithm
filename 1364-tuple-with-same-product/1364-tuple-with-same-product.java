class Solution {
    private static int ans;
    public int tupleSameProduct(int[] nums) {
        int N = nums.length;
        Map<Integer, Integer> map = new HashMap<>();
        int ans = 0;
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                int val = nums[i] * nums[j];
                ans += 8 * map.getOrDefault(val, 0);
                map.put(val, map.getOrDefault(val, 0) + 1);
                
            }
        }
        return ans;
    }

}