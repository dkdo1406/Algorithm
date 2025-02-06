import java.util.*;
import java.io.*;

public class Main {
    private static BufferedReader br;
    private static StringTokenizer st;
    private static StringBuilder sb;
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine().trim());
        sb = new StringBuilder();

        int N = Integer.parseInt(st.nextToken());
        int[] sticks = new int[N];
        for (int idx = 0; idx < N; idx++) {
            st = new StringTokenizer(br.readLine().trim());
            sticks[idx] = Integer.parseInt(st.nextToken());
        }
        int ans = 0;
        int height = 0;
        for (int idx = N - 1; idx >= 0; idx--) {
            if (height < sticks[idx]) {
                ans += 1;
                height = sticks[idx];
            }
        }

        System.out.println(ans);
    }
}
