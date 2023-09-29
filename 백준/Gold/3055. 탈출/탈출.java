import java.io.*;
import java.util.*;


/**
 * BOJ_3055_탈출_김형중
 * 
 * 비어있는곳 .
 * 물차있는곳 *
 * 돌 X
 * 비버굴 D, 고슴도치 S
 * 물이 매 분마다 비어있는 칸으로 확장
 * 물, 고슴도치는 돌을 통과하지 못함
 * 고슴도치는 물로 이동 불가
 * 물은 비버굴로 이동 불가
 * 고슴도치가 비버굴로 이동하기 위한 최소시간은?
 * 단, 고슴도치는 다음 분에 물이 차오르는 위치로 이동이 불가능하다.
 * (물이 먼저 차오르고 다음 고슴도치가 이동하면 될듯)
 * 
 * 
 * @author SSAFY
 *
 */
public class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static StringBuilder sb;

    static int N, M, ans;
    static char graph[][];
    static int dr[] = {1, -1, 0, 0};
    static int dc[] = {0, 0, -1, 1};


    public static void main(String[] args) throws Exception {
//        System.setIn(new FileInputStream("src/input.txt"));
        br = new BufferedReader(new InputStreamReader(System.in));

        sb = new StringBuilder();
        st = new StringTokenizer(br.readLine().trim());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        graph = new char[N][M];
        ans = -1;

        for (int r = 0; r < N; r++) {
            String s = br.readLine().trim();
            for (int c = 0; c < M; c++) {
                graph[r][c] = s.charAt(c);
            }
        }


        int action = 1;
        int cnt = 0;
        while(action == 1) {
            cnt += 1;
            // 물 이동
            wave();
            // 고슴도치 이동
            action = move();
//            System.out.println(cnt + " " + action);
//            for (int r = 0 ; r < N; r++) {
//                for (int c = 0; c < M; c++) {
//                    System.out.print(graph[r][c] + " ");
//                }
//                System.out.println();
//            }
            
        }


        // 출력
        if (action == -1) {
            System.out.println("KAKTUS");
        } else {
            System.out.println(cnt);
        }
        
        
        


    }


    /**
     * 물이 차오르는 
     */
    private static void wave() {
        int nr, nc, curr[];
        
        Queue<int[]> water = new ArrayDeque<>();
        
        for (int r = 0; r < N; r++) {
        	for (int c = 0; c< M; c++) {
        		if (graph[r][c] == '*') {
        			water.offer(new int[] {r, c});
        		}
        	}
        }
        
        while(!water.isEmpty()) {
        	curr = water.poll();
        	int r = curr[0];
            int c = curr[1];
            for (int dir = 0; dir < 4; dir++) {
                nr = r + dr[dir];
                nc = c + dc[dir];
                // 범위를 넘어가는 경우
                if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;

                // 돌, 비버굴, 기본 방문한 물인 경
                if (graph[nr][nc] == 'X' || graph[nr][nc] == 'D' || graph[nr][nc] == 'w') continue;

                // 고슴도치가 있는 곳인 경우 
                if (graph[nr][nc] == 'S' || graph[nr][nc] == 'W') {
                    graph[nr][nc] = 'W';
                } else {
                	graph[nr][nc] = '*';
                }
                

            }
        }

    }

    private static int move() {
        int nr, nc;

        // 현재 가지고 있는 비버들 이동
        int cnt = 0;
        Queue<int[]> q = new ArrayDeque<>();
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                if(graph[r][c] == 'S' || graph[r][c] == 'W') {
                    q.offer(new int[] {r, c});
//                    System.out.println(r + " " + c + " " + graph[r][c]);
                }
            }
        }
//        System.out.println(q);

        while(!q.isEmpty()) {
        
            int[] curr = q.poll();
            int r = curr[0];
            int c = curr[1];
            for (int dir = 0; dir < 4; dir++) {
                nr = r + dr[dir];
                nc = c + dc[dir];
                // 범위를 넘어가는 경우
                if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
                
//                System.out.println(nr + " " + nc + " " + graph[nr][nc]);
                // 비버굴인 경우 끝
                if (graph[nr][nc] == 'D') {
                	
                	graph[nr][nc] = 'A';
                    return 0; // 끝나면 0
                }
                
                // 돌, 물, 방문했었던 곳인 경우
                if (graph[nr][nc] == 'X' || graph[nr][nc] == '*' || graph[nr][nc] == 's') continue;

                
                graph[nr][nc] = 'S';
                cnt += 1;
            }
            if (graph[r][c] == 'W') {
                graph[r][c] = '*';
            } else {
                graph[r][c] = 's';
            }
        }




        if (cnt == 0) {
            // 더 이상 이동할 친구가 없으면 -1
            return -1;
        } else {
            // 아직 이동이 가능하면 1
            return 1;
        }
    }



}