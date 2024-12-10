class Solution {
    public int maximumLength(String s) {
        
        // 최대 연속 문자열 찾기
        // 최소 3번은 같은숫자가 나타나야 포함시킴.

        Set<Character> chars = new HashSet<>();
        Map<Character, Integer> charCnt = new HashMap<>();

        char curr = s.charAt(0);
        int maxCnt = 1;
        int ans = -1;
        int alpha;
        // 배열을 3중으로 만든다.
        int[][][] abc = new int[26][51][1];
        chars.add(curr);
        
        List temp = new LinkedList<Integer>();
        for (int i = 1; i < s.length(); i++) {
            chars.add(s.charAt(i));
            if (!charCnt.containsKey(curr)) {
                charCnt.put(curr, 0);
            }
            // 이전값과 다르다면
            if (curr != s.charAt(i)) {
                alpha = curr - 'a';
                
                charCnt.replace(curr, Math.max(charCnt.get(curr), maxCnt));
                for (int idx = 0; idx < maxCnt; idx++) {
                    abc[alpha][idx + 1][0] += maxCnt - idx;
                }

                curr = s.charAt(i);
                maxCnt = 1;
                
                // 마지막 값이라면
                if (i == s.length() - 1) {
                    if (!charCnt.containsKey(curr)) {
                        charCnt.put(curr, 0);
                    }
                    alpha = curr - 'a';
                    charCnt.replace(curr, Math.max(charCnt.get(curr), maxCnt));
                    for (int idx = 0; idx < maxCnt; idx++) {
                        abc[alpha][idx + 1][0] += maxCnt - idx;
                    }
                }

            } else {
                // 이전값과 같다면
                maxCnt += 1;
                
                // 마지막 값이라면
                if (i == s.length() - 1) {
                    charCnt.replace(curr, Math.max(charCnt.get(curr), maxCnt));
                    alpha = curr - 'a';
                    for (int idx = 0; idx < maxCnt; idx++) {
                        abc[alpha][idx + 1][0] += maxCnt - idx;
                    }
                }
            }
        }

        for (Character c : charCnt.keySet()) {
            int al = c - 'a';
            
            for (int idx = charCnt.get(c); idx >= 1; idx--) {
                if (abc[al][idx][0] >= 3) {
                    ans = Math.max(ans, idx);
                    break;
                }
            }
        }

        
        
       

        
        return ans;
    }
}