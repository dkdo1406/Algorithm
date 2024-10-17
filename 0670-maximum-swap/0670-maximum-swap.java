class Solution {
    public int maximumSwap(int num) {
        // 한번 스왑해서 가장 큰 숫자
        // 1. 가장 큰 숫자가 맨 앞이 아니라면 swap
        // 2. 모두 정렬이 되어 있으면 stop
        
        int ans = num;
        char[] s = Integer.toString(num).toCharArray();
        System.out.println(s);
        int maxValue = 0;
        char tmp;
        String temp;
        for (int l = 0; l < s.length - 1; l++) {
            for (int r = l + 1; r < s.length; r++) {
                tmp = s[l];
                s[l] = s[r];
                s[r] = tmp;
                temp = String.valueOf(s);
                ans = Math.max(ans, Integer.parseInt(temp));
                s[r] = s[l];
                s[l] = tmp;
            }
            
        }
        return ans;
    }
}