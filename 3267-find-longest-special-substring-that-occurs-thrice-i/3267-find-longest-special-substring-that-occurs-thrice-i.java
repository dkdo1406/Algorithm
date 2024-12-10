class Solution {
    public int maximumLength(String s) {
        
        // 최대 연속 문자열 찾기
        // 최소 3번은 같은숫자가 나타나야 포함시킴.

        Set<Character> chars = new HashSet<>();
        Map<Character, List<Integer>> charMap = new HashMap<>();
        Map<Character, Integer> charCnt = new HashMap<>();

        
        boolean check = false;
        char curr = s.charAt(0);
        int maxCnt = 1;
        int ans = -1;
        List temp = new LinkedList<Integer>();
        for (int i = 1; i < s.length(); i++) {
            if (curr != s.charAt(i)) {
                temp = new LinkedList<Integer>();
                if (!charMap.containsKey(curr)) {
                    temp.add(maxCnt);
                    charMap.put(curr, temp);
                } else {
                    temp = charMap.get(curr);
                    temp.add(maxCnt);
                    
                    charMap.replace(curr, temp);
                }
                

                curr = s.charAt(i);
                maxCnt = 1;
                if (i == s.length() - 1) {
                    if (!charMap.containsKey(curr)) {
                        charMap.put(curr, new LinkedList<Integer>());
                    }
                    temp = charMap.get(curr);
                    temp.add(maxCnt);
                    
                    charMap.replace(curr, temp);
                }

            } else {
                maxCnt += 1;
                if (i == s.length() - 1 && curr == s.charAt(i)) {
                    temp = charMap.get(curr);
                    temp.add(maxCnt);
                    
                    charMap.replace(curr, temp);
                }
            }
            
            if (chars.contains(curr)) {
                
                check = true;
            }
            chars.add(curr);
            if (!charMap.containsKey(curr)) {
                charMap.put(curr, new LinkedList<Integer>());
            }
            // System.out.println(curr);
        }

        // charMap.put(1, chars);
        
        int[] aa;
        for (Character c : charMap.keySet()) {
            aa = new int[51];
            System.out.println("시작");
            System.out.println(c);
            temp = charMap.get(c);
            System.out.println(temp);

            Collections.sort(temp);
            System.out.println(temp);
            if (temp == null) {
                continue;
            }
            Integer maxValue = (Integer)temp.getLast();
            // int minValue = temp.indexOf(1);
            System.out.println("minValue");
            System.out.println(maxValue);
            for (int i : (List<Integer>)temp) {
                for (int idx = 0; idx < i; idx++) {
                    aa[idx + 1] += i - idx;
                }
            }
            for (int idx = maxValue; idx >= 1; idx--) {
                if (aa[idx] >= 3) {
                    ans = Math.max(ans, idx);
                    break;
                }
            }
            System.out.println(Arrays.toString(aa));
        }
        
        System.out.println(check);
        
        
       

        
        return ans;
    }
}