import java.util.*;
import java.io.*;

/*
 * BOJ_2164_카드2_김형중
 *
 * N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오
 * 
 * 
 * 
 */
public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static StringBuilder sb;

	static int N;


	public static void main(String[] args) throws IOException {
//		System.setIn(new FileInputStream("src/input.txt"));

		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine().trim(), " ");
		sb = new StringBuilder();
		
		N = Integer.parseInt(st.nextToken()); // 카드 수
		int ans = 0;
		
		ArrayDeque<Integer> deque = new ArrayDeque<Integer>();

		for(int idx = 1; idx < N + 1; idx++) {
			deque.offer(idx);
		}
		
		for(int idx = 0; idx < N - 1; idx++) {
			deque.poll();
			deque.offer(deque.poll());
		}

		System.out.println(deque.poll());

	}
}
