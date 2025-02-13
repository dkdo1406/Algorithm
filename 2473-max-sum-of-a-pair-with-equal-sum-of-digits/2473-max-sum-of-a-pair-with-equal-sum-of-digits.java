class Solution {
    public int maximumSum(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        int ans = -1;
        int val = 0;
        int copyNum = 0;
        for (int num : nums) {
            copyNum = num;
            val = 0;
            while(copyNum > 0) {
                val += copyNum % 10;
                copyNum /= 10;
            }
            if(map.containsKey(val)) {
                ans = Math.max(ans, map.get(val) + num);
                if (map.get(val) < num) {
                    map.replace(val, num);
                }
            } else {
                map.put(val, num);
            }
        }

        return ans;
    }
}