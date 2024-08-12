class KthLargest {
    private static int K;
    private static int[] nums;
    private static Queue<Integer> q;
    public KthLargest(int k, int[] nums) {
        K = k;
        this.nums = nums;
        // k번째친구는 여기 넣어야 함
        q = new PriorityQueue<Integer>();
        for (int num : nums) {
            q.add(num);
        }
        while (q.size() > K) {
            q.poll();
        }
    }
    
    public int add(int val) {
        q.add(val);
        if (q.size() > K) q.poll();
        return q.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */