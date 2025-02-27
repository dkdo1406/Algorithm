class Solution {
    public int lenLongestFibSubseq(int[] arr) {
        // 가장긴 피보나치 개수
        int ans = 0;
        Set<Integer> set = new HashSet<>();
        for (int num : arr) {
            set.add(num);
        }
        int sum = 0;
        int val1 = 0;
        int val2 = 0;
        int cnt = 0;
        for(int l = 0; l < arr.length - 1; l++) {
            for(int r = l + 1; r < arr.length; r++) {
                val1 = arr[l];
                val2 = arr[r];
                sum = val1 + val2;
                cnt = 2;
                while(set.contains(sum)) {
                    val1 = val2;
                    val2 = sum;
                    sum = val1 + val2;
                    cnt += 1;
                }
                ans = Math.max(ans, cnt);
            }
        }
        
        if (ans == 2) return 0;
        return ans;
        

    }
}