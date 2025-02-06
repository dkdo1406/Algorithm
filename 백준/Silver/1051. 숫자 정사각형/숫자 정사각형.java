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
        int M = Integer.parseInt(st.nextToken());
        int[][] graph = new int[N][M];
        int ans = 1;
        for (int r = 0; r < N; r++) {
            st = new StringTokenizer(br.readLine().trim());
            String s = st.nextToken();
            for (int c = 0; c < M; c++) {
                graph[r][c] = s.charAt(c) - '0';
            }
        }

        int idx;
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                idx = 1;
                while (r + idx < N && c + idx < M) {
                    if (graph[r + idx][c] == graph[r+idx][c+idx] && graph[r][c] == graph[r][c+idx]) {
                        if (graph[r + idx][c] == graph[r][c]) {
                            ans = Math.max(ans, idx + 1);
                        }
                    }
                    idx += 1;
                }    
            }
            
        }

        System.out.println(ans * ans);
    }
}
