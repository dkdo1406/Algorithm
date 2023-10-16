import java.io.*;
import java.util.*;

/**
 * 피보나치 수의 확장
 *
 * 첫째 줄 양수이면 1, 0이면 0, 음수이면 -1
 * 둘째줄에는 절대값 출력
 *
 * n = 1이면 f(1) = f(0) + f(-1)
 * f(2) = f(1) - f(0)
 * f(3) = f(2)
 * f(0) = f(-1) + f(-2)
 * f(-1) = 1
 * f(-2) = -1
 * f(-1) = f(-2) + f(-3)
 * -1 + 2
 */
public class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static StringBuilder sb;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine().trim());

        // 첫번째 줄 출력

        int[] ans = new int[1000001];

        ans[0] = 0;
        ans[1] = 1;
        if (n > 0) {
            ans[2] = 1;
        } else {
            ans[2] = -1;
        }

        // 두뻔째 줄 출력
        if (n > 0) {
            for (int idx = 3; idx <= n; idx++) {
                ans[idx] = (ans[idx - 1] + ans[idx - 2]) % 1000000000;
            }
        } else {
            for (int idx = 3; idx <= Math.abs(n); idx++) {
                ans[idx] = (ans[idx - 2] - ans[idx - 1]) % 1000000000;
            }
        }


        if (n > 0) {
            sb.append(1).append("\n");
        } else if (n == 0) {
            sb.append(0).append("\n");
        } else {
            n = Math.abs(n);
            if (n % 2 == 0) {
                sb.append(-1).append("\n");
            } else {
                sb.append(1).append("\n");
            }
        }
//        System.out.println(Arrays.toString(ans));
        sb.append(Math.abs(ans[n]));
        System.out.println(sb);
    }
}