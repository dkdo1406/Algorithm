import java.util.*;
import java.io.*;

/*
 * BOJ_6987_월드컵_김형중
 *

 * 
 * 접근 방법
 * 
 */
public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static StringBuilder sb;
	
	static int result[][], checkResult[][], ans;
	static boolean isPossible;

	public static void main(String[] args) throws IOException {
//		System.setIn(new FileInputStream("src/input.txt"));

		br = new BufferedReader(new InputStreamReader(System.in));
//		st = new StringTokenizer(br.readLine().trim());
		sb = new StringBuilder();
		
		for (int cycle = 0; cycle < 4; cycle++) {
			st = new StringTokenizer(br.readLine().trim());
			result = new int[6][3];
			ans = 1;
			isPossible = false;
			for (int team = 0; team < 6; team++) {
				int win = Integer.parseInt(st.nextToken());
				int draw = Integer.parseInt(st.nextToken());
				int lose = Integer.parseInt(st.nextToken());
				result[team][0] = win;
				result[team][1] = draw;
				result[team][2] = lose;
				
				if(win + draw + lose != 5) ans = 0;
				
			}
			if (ans == 0) {
				sb.append(0).append(" ");
			} else {
				checkPlay(0, 0, 1);
				if (isPossible) {
					sb.append(1).append(" ");
				} else {
					sb.append(0).append(" ");
				}
			}
			
			
		}

		
		
		
		

		System.out.println(sb);

	}
	
	private static void checkPlay(int depth, int teamA, int teamB) {
		if (depth == 15) {
			isPossible = true;
			return;
		}
		// teamA를 모두 확인했으면 다음 팀으로 이
		if (result[teamA][0] == 0 && result[teamA][1] == 0 && result[teamA][2] == 0) {

			checkPlay(depth, teamA + 1, teamA + 2);
		}
		// teamA가 승리가 있을 경우 비교할 팀 탐색
		if (result[teamA][0] > 0 && result[teamB][2] > 0) {
			result[teamA][0] -= 1;
			result[teamB][2] -= 1;
			checkPlay(depth + 1, teamA, teamB + 1);
			result[teamA][0] += 1;
			result[teamB][2] += 1;
		}
		
		// teamA가 무승부가 있을 경우 비교할 팀 탐색
		if (result[teamA][1] > 0 && result[teamB][1] > 0) {
			result[teamA][1] -= 1;
			result[teamB][1] -= 1;
			checkPlay(depth + 1, teamA, teamB + 1);
			result[teamA][1] += 1;
			result[teamB][1] += 1;
		}
		
		// teamA가 패배가 있을 경우 비교할 팀 탐색
		if (result[teamA][2] > 0 && result[teamB][0] > 0) {
			result[teamA][2] -= 1;
			result[teamB][0] -= 1;
			checkPlay(depth + 1, teamA, teamB + 1);
			result[teamB][0] += 1;
			result[teamA][2] += 1;
		}
	}
}