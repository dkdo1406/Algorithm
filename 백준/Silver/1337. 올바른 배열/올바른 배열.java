import java.io.*;
import java.util.*;

/**
 * BOJ_2178_미로탐색_김형중
 *
 * 문제
 * 올바른 배열 : 원소 중 5개가 연속적인 것을 뜻함
 * 인접한 수의 차이가 1
 *
 *
 * 접근 방법
 * BFS를 사용하여 탐색.
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
        int res = 5;
        int ans = 5;
        while (l < N) {
            while (r < N && arr[l] + 4 >= arr[r]) {
                r += 1;
                res -= 1;
                ans = Math.min(ans, res);
            }
            res += 1;
            l += 1;
        }
//        System.out.println(Arrays.toString(arr));




        System.out.println(ans);
    }
}