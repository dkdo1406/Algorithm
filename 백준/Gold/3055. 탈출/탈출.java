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
 * 접근 방법
 * 
 * 실패한 접근 방법
 * static에 queue를 만들어 관리한다(메모리 초과)
 * 
 * 다른 방법
 * 메모리가 초과났기 때문에 최대한 local에서 연산을 끝내도록 변경
 * 물의 이동과 고슴도치의 이동함수를 각각 만들어 각 함수가 실행할 때
 * 모든 그래프를 탐색하여 이동을 관리한다.
 * 
 * 조금 더 빠른 방법
 * 물의 이동과 고슴도치가 이동할 때 각각 모든 위치를 탐색하는데
 * 물이 이동할때 물의 위치와 고슴도치 위치를 모두 저장하여 사용
 * 물 이동 함수안에 고슴도치 이동 함수를 만들어 이동을 관리한다.
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

		// 액션초기세팅
		int action = 1;
		// 총 이동 횟수
		int cnt = 0;
		while(action == 1) {
			cnt += 1;
			// 홍수 시작 
			action = wave();
		}


		// 출력
		if (action == -1) {
			System.out.println("KAKTUS");
		} else {
			System.out.println(cnt);
		}

	}


	/**
	 * 물이 차오르는 함수
	 */
	private static int wave() {
		int nr, nc, curr[];

		Queue<int[]> water = new ArrayDeque<>();
		Queue<int[]> hedgehog = new ArrayDeque<>();
		for (int r = 0; r < N; r++) {
			for (int c = 0; c< M; c++) {
				if(graph[r][c] == 'S') {
					hedgehog.offer(new int[] {r, c});
				}
				else if (graph[r][c] == '*') {
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
				if (graph[nr][nc] == 'X' || graph[nr][nc] == 'D' || graph[nr][nc] == 'V') continue;

				graph[nr][nc] = '*';

			}
		}
		return move(hedgehog);

	}

	private static int move(Queue<int[]> hedgehog) {
		int r, c, nr, nc;

		// 이동한 고슴도치 수
		int cnt = 0;

		// 위에서 찾은 고슴도치들 사방탐색
		while(!hedgehog.isEmpty()) {

			int[] curr = hedgehog.poll();
			r = curr[0];
			c = curr[1];
			for (int dir = 0; dir < 4; dir++) {
				nr = r + dr[dir];
				nc = c + dc[dir];
				// 범위를 넘어가는 경우
				if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;

				// 비버굴인 경우 끝
				if (graph[nr][nc] == 'D') {
					return 0; // 끝나면 0
				}

				// 돌, 물, 방문했었던 곳인 경우
				if (graph[nr][nc] == 'X' || graph[nr][nc] == '*' || graph[nr][nc] == 'v') continue;


				graph[nr][nc] = 'S';
				cnt += 1;
			}
			// 방문했다고 표시
			if (graph[r][c] =='S') {
				graph[r][c] = 'v';
			}

		}


		if (cnt == 0) {
			// 더 이상 이동할 곳이 없다면
			return -1;
		} else {
			// 아직 이동이 가능한 곳이 있다면 1
			return 1;
		}
	}



}