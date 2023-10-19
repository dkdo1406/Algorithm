import java.io.*;
import java.util.*;

/**
 * BOJ_2178_미로탐색_김형중
 *
 * 문제
 * N * M 미로
 * 1,1 -> N,M에 도착하는 최소 칸수
 *
 * 접근 방법
 * BFS를 사용하여 탐색.
 *
 */
public class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static StringBuilder sb;

    static int N, M, graph[][];
    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    public static void main(String[] args) throws IOException {
//        System.setIn(new FileInputStream("src/input.txt"));
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine().trim());
        sb = new StringBuilder();
        // N, M
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        graph = new int[N][M];

        for (int r = 0; r < N; r++) {
            String S = br.readLine().trim();
            for (int c = 0; c < M; c++) {
                graph[r][c] = S.charAt(c) - '0';
            }
        }

        BFS();

        System.out.println(graph[N - 1][M - 1]);
    }
    private static void BFS() {
        // BFS 탐색 시작은 0,0
        Deque<Integer[]> queue = new ArrayDeque<>();
        queue.offer(new Integer[] {0, 0});

        int r, c, nr, nc;
        while (!queue.isEmpty()) {
            Integer[] pos = queue.poll();
            r = pos[0];
            c = pos[1];
            for (int dir = 0; dir < 4; dir++) {
                nr = r + dr[dir];
                nc = c + dc[dir];
                // 범위 넘어가면 continue
                if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
                // 벽이거나 이전에 방문한 위치면 pass
                if (graph[nr][nc] == 0 || graph[nr][nc] > 1) continue;
                graph[nr][nc] += graph[r][c];
                // 도착했으므로 리턴
                if (nr == N - 1 && nc == M - 1) return;
                queue.offer(new Integer[] {nr, nc});
            }
        }
    }
}