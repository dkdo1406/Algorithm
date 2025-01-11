import java.util.Map.Entry;
class Solution {
    public List<String> wordSubsets(String[] words1, String[] words2) {
        // delete
        List<String> ans = new LinkedList<>();
        Map<Character, Integer> dic = new HashMap<>();
        Map<Character, Integer> temp = new HashMap<>();

        Set<Character> alpha = new HashSet<>();
        Set<Character> comp = new HashSet<>();
        for (String s : words2) {
            temp = new HashMap<>();
            for (int idx = 0; idx < s.length(); idx++) {
                alpha.add(s.charAt(idx));
                if (!temp.containsKey(s.charAt(idx))) {
                    temp.put(s.charAt(idx), 1);
                } else {
                    temp.replace(s.charAt(idx), temp.get(s.charAt(idx)) + 1);
                }
            }
            for (Entry<Character, Integer> entrySet : temp.entrySet()) {
                if (!dic.containsKey(entrySet.getKey())) {
                    dic.put(entrySet.getKey(), entrySet.getValue());
                } else {
                    int cnt = dic.get(entrySet.getKey());
                    if (cnt < entrySet.getValue()) {
                        dic.replace(entrySet.getKey(), entrySet.getValue());
                    }
                }
            }
        }

        for (String s : words1) {
            temp = new HashMap<>();
            comp = new HashSet<>();
            for (int idx = 0; idx < s.length(); idx++) {
                comp.add(s.charAt(idx));
                if (!temp.containsKey(s.charAt(idx))) {
                    temp.put(s.charAt(idx), 1);
                } else {
                    temp.replace(s.charAt(idx), temp.get(s.charAt(idx)) + 1);
                }
            }
            // check alpha
            if (!comp.containsAll(alpha)) continue;
            // check count
            if (check(dic, temp)) {
                ans.add(s);
            }
        }

        return ans;
    }

    public boolean check(Map<Character, Integer> dic, Map<Character, Integer> b) {
        
        for (Entry<Character, Integer> entrySet : dic.entrySet()) {
            // System.out.println("???????" + " " + s);
            char c = entrySet.getKey();
            int cnt = entrySet.getValue();
            // System.out.println(s + " " + b.get(c) + " " + cnt);
            if (b.get(c) < cnt) return false;
        }
        return true;
    }
}