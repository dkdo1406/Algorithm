class Solution {
    public boolean canConstruct(String s, int k) {
        // s, k; all c in s palindrome
        // 짝수로 존재할 경우 가능
        // 홀수로 존재할 경우 단독 불가능
        // 홀수로 존재하는게 몇개있는지 확인
        boolean ans = true;
        if (s.length() < k) return false;
        char[] c = s.toCharArray();
        Arrays.sort(c);
        int cnt = 0;
        int check = 0;
        char ch = 'A';
        for (int idx = 0; idx < c.length; idx++) {
            if (ch != c[idx]) {
                if (cnt % 2 == 1) {
                    check += 1;
                }
                cnt = 0;
                ch = c[idx];
            }
            cnt += 1;
        }
        if (cnt % 2 == 1) {
            check += 1;
        }
        // System.out.println(check);
        if (check > k) {
            ans = false;
        }
        return ans;
    }
}