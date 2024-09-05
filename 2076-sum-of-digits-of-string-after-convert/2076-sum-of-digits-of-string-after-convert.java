
class Solution {
    private static StringBuilder sb;
    public int getLucky(String s, int k) {
        sb = new StringBuilder();        
        for (char val : s.toCharArray()) {
            sb.append(val - 'a' + 1);
        }
        for (int idx = 0; idx < k; idx++) {
            transform();
        }
        int res =  Integer.parseInt(sb.toString());
        return res;
    }
    void transform() {
        int sum = 0;
        for (int idx = 0; idx < sb.length(); idx++) {
            sum += sb.charAt(idx) - '0';
        }
        sb = new StringBuilder();
        sb.append(sum);
    }

    
}