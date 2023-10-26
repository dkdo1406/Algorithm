import java.io.*;
import java.util.*;


/**
 * BOJ_1931_회의실배정_김형중
 *  
 * 문제N개 회의실 사용표시작시간 끝나는시간, 곂치지 않게 하며
 * 회의실을 사용할 수 있는 회의의 최대 개수는?
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
		
		PriorityQueue<Point> queue = new PriorityQueue<Point>();
		for (int idx = 0; idx < N; idx++) {
			st = new StringTokenizer(br.readLine().trim());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			queue.add(new Point(start, end));
		}
		int ans = 0;
		int time = -1;
		while (!queue.isEmpty()) {
			Point point = queue.poll();
			if (time <= point.start) {
				time = point.end;
				ans += 1;
				
			}
		}
		
		System.out.println(ans);

	}

}

class Point implements Comparable<Point>{
	int start, end;
	public Point(int start, int end) {
		this.start = start;
		this.end = end;
	}
	
	@Override
		public int compareTo(Point o) {
			if (this.end != o.end) {
				return this.end < o.end ? -1 : 1;
			}
			return this.start < o.start ? -1 : 
				1;
			
		}
	
}