import java.io.*;
import java.util.*;


/**
 * BOJ_1347_미로만들기_김형중
 *  
 * 문제
 * 남쪽을 보고 시작
 * 이동할 수 있는 곳만 이동함
 * F는 앞으로 한칸 L과 R은 방향을 왼쪽 또는 오른쪽으로 전환한 것
 * 
 * 
 * @author
 *
 */
public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static StringBuilder sb;

	static int T, N, M;
	static String ans;

	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("src/s_input.txt"));
		br = new BufferedReader(new InputStreamReader(System.in));
		
		sb = new StringBuilder();
		N = Integer.parseInt(br.readLine().trim());
		
		int[] dr = {1, 0, -1, 0};
		int[] dc = {0, 1, 0, -1};
		int dir = 0;
		
		String[][] graph = new String[100][100];
		// 시작은 50,50으로
		int minR = 50;
		int maxR = 50;
		int minC = 50;
		int maxC = 50;
		int r = 50;
		int c = 50;
		graph[r][c] = ".";
		String s = br.readLine().trim();
		for (int idx = 0; idx < N; idx++) {
			String S = String.valueOf(s.charAt(idx));
			if (S.equals("F")) {
				r = r + dr[dir];
				c = c + dc[dir];
				graph[r][c] = ".";
				minR = Math.min(minR, r);
				maxR = Math.max(maxR, r);
				minC = Math.min(minC, c);
				maxC = Math.max(maxC, c);

			} else if(S.equals("L")) {
				dir = (dir + 1) % 4;

			} else if(S.equals("R")) {
				dir = (dir - 1);
				if (dir < 0) {
					dir = 3;
				}
			}
		}

		for (int R = minR; R <= maxR; R++) {
			for (int C = minC; C <= maxC; C++) {
				if (graph[R][C] == null) {
					sb.append("#");
				} else {
					sb.append(".");
				}
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}

}