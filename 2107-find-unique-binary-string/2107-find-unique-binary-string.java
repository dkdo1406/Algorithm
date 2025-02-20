class Solution {
    public String findDifferentBinaryString(String[] nums) {
        // 문자 -> 이진법
        Arrays.sort(nums);
        int N = nums[0].length();
        int curr = 0;
        for(String num : nums) {
            if(curr != Integer.parseInt(num, 2)) {
                return String.format("%0"+N+"d", Integer.parseInt(Integer.toBinaryString(curr)));
            }
            
            curr += 1;
        }
        return String.format("%0"+N+"d", Integer.parseInt(Integer.toBinaryString(curr)));
    }
}