import java.util.*;
class Solution {
    static int[] arr;
    static int answer;
    static int N;
    public int solution(int[] picks, String[] minerals) {
        // 곡괭이 각각 0~5개 캘때마다 피로도 소모
        // 한번 곡괭이를 선택하면 곡괭이를 사용할 . 쉉ㅂㅅ을때까지
        for (int idx = 0; idx < 3; idx++) {
            N += picks[idx];
        }
        
        answer = minerals.length * 25;
        arr = new int[N];
        permutation(0, arr, picks, minerals);
        return answer;
    }
    
    static void permutation(int depth, int[] arr, int[] picks, String[] minerals) {
        // 종료조건 : 곡괭이 모두 소모 or 더이상 캘것이 없으면
        if (depth == N) {
            int mineIdx = 0;
            int res = 0;
            for (int idx = 0; idx < minerals.length; idx++) {
                if (idx != 0 && idx % 5 == 0) {
                    mineIdx += 1;
                    if (mineIdx == N) break;
                }
                // 현재 선택
                String mineral = minerals[idx];
                // 0 : 다이아, 1: 철, 2: 돌
                int mine = arr[mineIdx];
                if (mine == 0) {
                    res += 1;
                } else if (mine == 1) {
                    if (mineral.equals("diamond")) {
                        res += 5;
                    } else {
                        res += 1;
                    } 
                } else {
                    if (mineral.equals("diamond")) {
                        res += 25;
                    } else if (mineral.equals("iron")) {
                        res += 5;
                    } else {
                        res += 1;
                    }
                }

            }

            answer = Math.min(answer, res);
            return;
        }
        
        for (int idx = 0; idx < 3; idx++) {
            if (picks[idx] == 0) continue;
            arr[depth] = idx;
            picks[idx] -= 1;
            permutation(depth + 1, arr, picks, minerals);
            picks[idx] += 1;
        }
    }
}