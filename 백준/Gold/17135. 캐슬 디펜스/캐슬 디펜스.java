import java.util.*;
import java.io.*;

/**
 * BOJ_17135_캐슬디펜스_김형중
 * 
 * 격자판의 상태가 주어졌을 때, 궁수의 공격으로 제거할 수 있는 적의 최대 수를 계산해보자.
 * 
 * 접근 방법
 * 방문 체크를 하기 위해 Set을 전역으로 선언
 * 상,하,좌,우를 보며 방문할 수 있다면 visit에 추가
 * 방문을 못할경우 ans를 visit의 개수와 비교하여 큰 값으로 저장
 * 
 * @author SSAFY
 *
 */
public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static StringBuilder sb;

	static int graph[][], dr[], dc[], N, M, D, ans, archer[];
	static Set<Point> attack;

	public static void main(String[] args) throws IOException {
//		System.setIn(new FileInputStream("src/input.txt"));
		
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine().trim());
		sb = new StringBuilder();

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		D = Integer.parseInt(st.nextToken());
		graph = new int[N][M];

		
		// 우선 위로 올라가고 탐색하기 때문에
		// 왼쪽, 위, 오른쪽을 순서로 탐색한다.
		dr = new int[] {0, -1, 0};
		dc = new int[] {-1, 0, 1};
		archer = new int[3]; 
		ans = 0;
		for (int r = 0; r < N; r++) {
			st = new StringTokenizer(br.readLine().trim());
			for (int c = 0; c < M; c++) {
				graph[r][c] = Integer.parseInt(st.nextToken());
			}
		}
		
		combination(0, 0);

		System.out.println(ans);

	}
	
	private static void combination(int depth, int start) {
		if (depth == 3) {
			// 3곳 선택 완료 시뮬레이션 시작 
			simulation();
			return;
		}
		
		for (int idx = start; idx < M; idx++) {
			archer[depth] = idx;
			combination(depth + 1, start + 1);
		}
		
	}
	
	private static void shoot(int[][] tempGraph, Point p) {
		int r, c, nr, nc;
		Queue<Point> queue = new ArrayDeque<Point>();
		queue.offer(p);
		
		Set<Point> visit = new HashSet<>();
		while (!queue.isEmpty()) {
			Point point = queue.poll();
			r = point.r;
			c = point.c;
			
			for (int idx = 0; idx < 3; idx++) {
				nr = r + dr[idx];
				nc = c + dc[idx];
				
				// 그래프 범위를 넘어가거나 방문기록이 있으면 무시
				if (nr < 0 || nc < 0 || nc >= M || visit.contains(new Point(nr, nc))) continue;
				
				// 범위를 넘어가는 경우 탈출
				if (D  < Math.abs(p.r + 1 - nr) + Math.abs(p.c - nc)) return;
				
				// 찾을 경우 HashMap에 저장 후 탈출
				if (tempGraph[nr][nc] == 1) {
					attack.add(new Point(nr, nc));
					return;
				}
				visit.add(new Point(nr, nc));
				queue.offer(new Point(nr, nc));
			}
		}
	}
	
	/**
	 * 모든 경우의 수를 보며 확인
	 */
	private static void simulation() {
		int[][] tempGraph = new int[N][M];
		int res = 0;
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < M; c++) {
				tempGraph[r][c] = graph[r][c];
			}
		}

		for (int line = N; line > 0; line--) {
			if (ans >= res + line * 3) return;
			attack = new HashSet<>();
			for (int idx = 0; idx < 3; idx++) {
				if (tempGraph[line - 1][archer[idx]] == 1) {
					attack.add(new Point(line - 1, archer[idx]));
				} else {
					shoot(tempGraph, new Point(line - 1, archer[idx]));	
				}
				

			}
			// 찾는 것이 끝나면 결과값에서 추가 후 그래프에서 삭제
			res += attack.size();
			Iterator<Point> iter = attack.iterator();
			while (iter.hasNext()) {
				Point point = iter.next();
				tempGraph[point.r][point.c] = 0;
			}
		}
		ans = Math.max(ans, res);
	}
	

}

class Point {
	int r, c;
	public Point(int r, int c) {
		this.r = r;
		this.c = c;
	}
	
	@Override
	public boolean equals(Object obj) {
		if (this == obj) return true;
		if (!(obj instanceof Point)) return false;
		Point point = (Point)obj;
		return r == point.r && Objects.equals(point.c, c);
	}
	
	@Override
	public int hashCode() {
		return Objects.hash(r, c);
	}

	@Override
	public String toString() {
		return "Point [r=" + r + ", c=" + c + "]";
	}
}