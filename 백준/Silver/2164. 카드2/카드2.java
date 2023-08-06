import java.util.*;
import java.io.*;

/*
 * BOJ_2164_카드2_김형중
 *
 * N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오
 * 
 * 구현
 * ArrayDeque에 1부터 N까지의 값을 넣는다.
 * 가장 앞에 값은 빼고, 그 다음 값은 가장 뒤에 넣는다.
 * 이를 N - 1번 반복한다.
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
		
		// 가장 앞에 값을 O(1)속도로 빼기 위해 deque자료구조를 사용
		ArrayDeque<Integer> deque = new ArrayDeque<Integer>();

		// 1부터 N까지 값을 넣는다.
		for(int idx = 1; idx < N + 1; idx++) {
			deque.offer(idx);
		}
		
		// 가장 앞에 값을 빼고, 그 다음 값을 제일 뒤로 넣는다.
		for(int idx = 0; idx < N - 1; idx++) {
			deque.poll();
			deque.offer(deque.poll());
		}

		// 마지막으로 남은 값을 뽑는다.
		sb.append(deque.poll());
		
		System.out.println(sb);

	}
}
