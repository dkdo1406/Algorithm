import java.io.*;
import java.util.*;


/**
 * BOJ_2239_스도쿠_김형중
 * 
 * 이진 탐색의 조건 : 정렬된 상황
 * 가장 긴 증가하는 부분 수열을 만들어야 하기 때문에 정렬되어 있는 상황을
 * 계속 만든다. 그렇기에 이진 탐색을 사용하면 쉽게 사용이 가능하다.
 * 
 * 
 * @author SSAFY
 *
 */
public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static StringBuilder sb;
	static final int N = 9;
	static int graph[][] = new int[N][N];
	static List<Point> zero;
	static Set<Integer>[] row, col, threee;
	static Map<Point, Integer> dic;

	public static void main(String[] args) throws Exception {
		//		System.setIn(new FileInputStream("src/input.txt"));
		br = new BufferedReader(new InputStreamReader(System.in));

		sb = new StringBuilder();

		// 스도쿠 규칙에 맞는지 확인하기 위한 Set
		// row, col, 해당 3*3에 중복 숫자가 없으면 정답임
		row = new HashSet[N];
		col = new HashSet[N];
		threee = new HashSet[N];

		dic = new HashMap<Main.Point, Integer>();
		zero = new ArrayList<Main.Point>();

		for (int idx = 0; idx < N; idx++) {
			row[idx] = new HashSet<>();
			col[idx] = new HashSet<>();
			threee[idx] = new HashSet<>();
		}
		int cnt = 0;
		for (int r = 0; r < 9; r += 3) {
			for (int c = 0; c < 9; c+= 3) {
				dic.put(new Point(r, c), cnt++);
			}
		}
		// 0,0 -> 0 0,3 ->2... 이런 식으로
		// 배열에 넣
		// 스도쿠 입력받기
		for (int r = 0; r < N; r++) {
			String S = br.readLine().trim();
			for (int c = 0; c < N; c++) {
				graph[r][c] = S.charAt(c) - '0';
				if (graph[r][c] == 0) {
					zero.add(new Point(r, c));
				} else {
					row[r].add(graph[r][c]);
					col[c].add(graph[r][c]);
					threee[dic.get(new Point(r - (r % 3), c - (c % 3)))].add(graph[r][c]);
				}
			}
		}
		PriorityQueue<Pos> pos = new PriorityQueue<Main.Pos>();
		for (Point point : zero) {
			int count = 0;
			count += row[point.r].size();
			count += col[point.c].size();
			count += threee[dic.get(new Point(point.r - (point.r % 3), point.c - (point.c % 3)))].size();
			pos.offer(new Pos(count, point));
		}

		// 아직 안정해진 곳에 빈 값 넣
		DFS(0);
		//		System.out.println(sb);

	}

	private static void DFS(int depth) {
		// 종료 조건 : 모든 빈 칸을 채웠을 경우 종료

		if(depth == zero.size()) {
			for (int r = 0; r < N; r++) {
				for (int c = 0; c < N; c++) {
					sb.append(graph[r][c]);
				}
				sb.append("\n");
			}
			System.out.println(sb);
			System.exit(0);
			return;
		}





//		for(int idx = index; idx < zero.size(); idx++) {

			int r = zero.get(depth).r;
			int c = zero.get(depth).c;
//			System.out.println(r + " " + c);
			int three = dic.get(new Point(r - (r % 3), c - (c % 3)));
			for (int number = 1; number <= 9; number++) {
				if(row[r].contains(number) || col[c].contains(number) || threee[three].contains(number)) {
					continue;
				}
				row[r].add(number);
				col[c].add(number);
				threee[three].add(number);
				graph[r][c] = number;
				DFS(depth + 1);
				row[r].remove(number);
				col[c].remove(number);
				threee[three].remove(number);
				graph[r][c] = 0;
			}
//		}

		//pos.add(position);





	}
	static class Pos implements Comparable<Pos> {
		Point point;
		int count;
		public Pos(int count, Point point) {
			this.count = count;
			this.point = point;
		}

		@Override
		public int compareTo(Main.Pos o) {
			return this.count > o.count ? -1 : 1;
		}
	}


	static class Point {
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
			return this.r == point.r && Objects.equals(this.c, point.c);
		}

		@Override
		public int hashCode() {
			return Objects.hash(r, c);
		}
	}
}