import java.io.*;
import java.util.*;
class Solution {
    public String[] solution(String[] players, String[] callings) {
        String[] answer = {};
        int idx;
        String tmp;
        idx = 0;
        Map<String, Integer> dic = new HashMap<String, Integer>();
        for (String s : players) {
            dic.put(s, idx++);
        }
        
        for (String s : callings) {
            idx = dic.get(s);
            tmp = players[idx - 1];
            players[idx - 1] = players[idx];
            players[idx] = tmp;
            dic.put(players[idx - 1], idx - 1);
            dic.put(players[idx], idx);
        }
        return players;
    }
}