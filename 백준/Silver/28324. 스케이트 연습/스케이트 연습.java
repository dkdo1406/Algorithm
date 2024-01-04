import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static StringBuilder sb;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine().trim());
        sb = new StringBuilder();

        int N = Integer.parseInt(st.nextToken());
        int speed[] = new int[N];
        long ans = 0;

        st = new StringTokenizer(br.readLine().trim());
        for (int idx = 0; idx < N; idx++) {
            // 각 구간 낼 수 있는 속력
            speed[idx] = Integer.parseInt(st.nextToken());
        }
        // 도착속도는 0이다.
        int currentSpeed = 0;
        for (int idx = N - 1; idx >= 0; idx--) {
            // 역순으로 확인
            currentSpeed = Math.min(currentSpeed + 1, speed[idx]);
            ans += currentSpeed;
        }
        System.out.println(ans);

    }
}