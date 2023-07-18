import java.io.*;
import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        int res = 0;
        Map<String, Integer> dic = new HashMap<String, Integer>();
        for (int idx = 0; idx < name.length; idx++) {
            dic.put(name[idx], yearning[idx]);
        }
        
        for (int idx = 0; idx < photo.length; idx++) {
            res = 0;
            for (int score = 0; score < photo[idx].length; score++) {
                if (dic.containsKey(photo[idx][score])) {
                    res += dic.get(photo[idx][score]);    
                }
            }
            answer[idx] = res;
        }
        
        return answer;
    }
}