class Solution {
    public long pickGifts(int[] gifts, int k) {
        Queue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
        long ans = 0;
        for (int gift : gifts) {
            q.offer(gift);
        }
        while(k != 0) {
            int gift = q.poll();
            q.offer((int)Math.sqrt(gift));
            k--;
        }
        
        while (q.size() != 0) {
            ans += q.poll();
        }
        
        return ans;
    }
}