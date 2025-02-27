class Solution {
    public int lenLongestFibSubseq(int[] arr) {
        // 가장긴 피보나치 개수
        int ans = 0;
        Map<Integer, Integer> map = new HashMap<>();
        Set<Integer> set = new HashSet<>();
        for (int num : arr) {
            map.put(num, 0);
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
                while(map.containsKey(sum)) {
                    // 피보나치 시작
                    map.replace(sum, Math.max(map.get(sum), map.get(val1) + 1));
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