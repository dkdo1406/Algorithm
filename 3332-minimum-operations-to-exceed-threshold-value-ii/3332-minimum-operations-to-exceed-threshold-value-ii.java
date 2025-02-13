class Solution {
    public int minOperations(int[] nums, int k) {
        int ans = 0;
        Queue<Double> q = new PriorityQueue<>();

        for(int num : nums) {
            q.offer((double)num);
        }
        double a,b;
        while(q.size() > 0) {
            a = q.poll();
            if(a >= k) break;
            b = q.poll();
            q.offer(a * 2 + b);
            ans += 1;
        }


        return ans;
    }
}