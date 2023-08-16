import java.util.*;
import java.io.*;

/*
 * BOJ_6987_월드컵_김형중
 *
 * 
 * 접근 방법
 * result라는 2차원배열을 6 * 3로 초기화하여 모든 경기를 저장한다.
 * 첫번째 있는 팀부터 시작하여 다른 팀과 경기를 할 수 있는 상태인지 확인을 한다.
 * teamA가 승리가 있다면 teamB는 패배가 있어야 경기를 할 수 있는 상태이다.
 * 이를 반복하여 서로 가능한 상태인지 체크하고 깊이가 15가 되면 가능하다는 플레그를 저장한다.
 * 
 */
public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static StringBuilder sb;
	
	static int result[][];
	static boolean isPossible;

	public static void main(String[] args) throws IOException {
//		System.setIn(new FileInputStream("src/input.txt"));

		br = new BufferedReader(new InputStreamReader(System.in));
//		st = new StringTokenizer(br.readLine().trim());
		sb = new StringBuilder();
		
		for (int idx = 0; idx < 4; idx++) {
			st = new StringTokenizer(br.readLine().trim());
			result = new int[6][3];

			isPossible = true;
			for (int team = 0; team < 6; team++) {
				int win = Integer.parseInt(st.nextToken());
				int draw = Integer.parseInt(st.nextToken());
				int lose = Integer.parseInt(st.nextToken());
				result[team][0] = win; // 승리
				result[team][1] = draw; // 비김
				result[team][2] = lose; // 패배
				
				// 경기의 합이 5가 안되는 경우는 불가
				if(win + draw + lose != 5) isPossible = false;
				
			}
			
			if (isPossible) {
				// 진짜 경기가 있는지 확인을 위해 초기화
				isPossible = false;
				checkPlay(0, 0, 1);
				// 최종 확인
				if (isPossible) {
					sb.append(1).append(" ");
					continue;
				}
			}
			// 불가능
			sb.append(0).append(" ");
			
		}


		System.out.println(sb);

	}
	
	/**
	 * 경기가 있는지 확인하는 함수
	 * teamA와 teamB의 경기를 비교하여 각 경기가 서로 맞아떨어지면 teamB를 1추가한다.
	 * @param depth
	 * @param teamA
	 * @param teamB
	 */
	private static void checkPlay(int depth, int teamA, int teamB) {
		
		// 15경기 모두 확인을 했다면 isPossible를 true로 바꾸고 탈출
		if (depth == 15) {
			isPossible = true;
			return;
		}
		// teamA를 모두 확인했으면 다음 팀으로 이동
		if (result[teamA][0] == 0 && result[teamA][1] == 0 && result[teamA][2] == 0) {
			
			checkPlay(depth, teamA + 1, teamA + 2);
		}
		// teamA가 승리가 있을 경우 패배가 있는 팀 탐색
		if (result[teamA][0] > 0 && result[teamB][2] > 0) {
			result[teamA][0] -= 1;
			result[teamB][2] -= 1;
			checkPlay(depth + 1, teamA, teamB + 1);
			result[teamA][0] += 1;
			result[teamB][2] += 1;
		}
		
		// teamA가 무승부가 있을 경우 무승부가 있는 팀 탐색
		if (result[teamA][1] > 0 && result[teamB][1] > 0) {
			result[teamA][1] -= 1;
			result[teamB][1] -= 1;
			checkPlay(depth + 1, teamA, teamB + 1);
			result[teamA][1] += 1;
			result[teamB][1] += 1;
		}
		
		// teamA가 패배가 있을 경우 승리가 있는 팀 탐색
		if (result[teamA][2] > 0 && result[teamB][0] > 0) {
			result[teamA][2] -= 1;
			result[teamB][0] -= 1;
			checkPlay(depth + 1, teamA, teamB + 1);
			result[teamB][0] += 1;
			result[teamA][2] += 1;
		}
	}
}