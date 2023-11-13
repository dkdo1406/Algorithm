import java.io.*;
import java.util.*;

/**
 * BOJ_1337_올바른 배열_김형중
 *
 * 문제
 * 올바른 배열 : 원소 중 5개가 연속적인 것을 뜻함
 * 인접한 수의 차이가 1
 *
 *
 * 접근 방법
 * 배열에 모두 받은 후 오름차순으로 정렬한다.
 * 투 포인터를 사용하여 arr[l]에 맞는지 확인한다.
 *
 */
public class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static StringBuilder sb;

    static int N, M;
    public static void main(String[] args) throws IOException {
//        System.setIn(new FileInputStream("src/input.txt"));
        br = new BufferedReader(new InputStreamReader(System.in));
//        st = new StringTokenizer(br.readLine().trim());
        sb = new StringBuilder();
        // N, M

        N = Integer.parseInt(br.readLine().trim());
        int[] arr = new int[N];
        for (int idx = 0; idx < N; idx++) {
            M = Integer.parseInt(br.readLine().trim());
            arr[idx] = M;
        }
        Arrays.sort(arr);
        int l = 0;
        int r = 0;
        int res = 5; // 시작값
        int ans = 5; // 결과 최대값
        while (l < N) {
            // arr[l]이 기준값이며 arr[r]이 이 안에 들어는지 확인한다.
            while (r < N && arr[l] + 4 >= arr[r]) {
                // 올바른 배열이 맞다면 r을 1 증가시켜주고 결과값을 1을 감소시킨다.
                r += 1;
                res -= 1;
            }
            // 결과값중 최소값으로 입력한다.
            ans = Math.min(ans, res);
            // 모든 비교가 끝났기에 다시 1 증가시켜준다.
            res += 1;
            l += 1;
        }

        System.out.println(ans);
    }
}