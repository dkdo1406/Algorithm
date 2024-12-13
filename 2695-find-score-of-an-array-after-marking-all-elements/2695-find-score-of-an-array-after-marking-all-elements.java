class Solution {
    public long findScore(int[] nums) {
        Queue<Element> q = new PriorityQueue<>();
        Set<Integer> chosen = new HashSet<>();

        long ans = 0;
        for (int idx = 0; idx < nums.length; idx++) {
            q.offer(new Element(nums[idx], idx));
        }

        while(q.size() != 0) {
            Element e = q.poll();
            if (chosen.contains(e.index)) continue;
            chosen.add(e.index);
            chosen.add(e.index - 1);
            chosen.add(e.index + 1);
            ans += e.num;
        }

        return ans;
    }
}


// 정의하기
class Element implements Comparable<Element> {
    int num, index;

    public Element(int num, int index) {
        this.num = num;
        this.index = index;
    }

    public int compareTo(Element e) {
        if (this.num < e.num) {
            return -1;
        } else if (this.num > e.num) {
            return 1;
        } else {
            if (this.index < e.index) {
                return -1;
            } else {
                return 1;
            }
        }
    }   
}