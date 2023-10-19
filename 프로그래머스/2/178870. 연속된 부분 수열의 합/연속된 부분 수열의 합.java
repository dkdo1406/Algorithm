class Solution {
    public int[] solution(int[] sequence, int k) {
        
        
        // l : 시작, r : 끝 지점
        // 
        int l = 0;
        int r = 0;
        int n = sequence.length;
        int res = 0;
        int[] answer = {0, n - 1};
        while (l < n) {
            
            // 크기가 작으면 추가
            while (res < k && r < n) {
                res += sequence[r];
                r += 1;
            }
            // 결과를 찾았으면 현재 정답과 비교
            if (res == k) {
                if (r == 1) {
                    return new int[] {0, 0};
                }
                if(answer[1] - answer[0] > (r - 1) - l) {
                    answer[0] = l;
                    answer[1] = r - 1;
                }
            }
            res -= sequence[l];
            l += 1;
        }
        return answer;
    }
}