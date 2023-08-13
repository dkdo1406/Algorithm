import java.util.*;
import java.io.*;

/*
 * BOJ_1655_숫자놀이_김형중
 *

 * 
 * 접근 방법
 * 
 */
public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static StringBuilder sb;

	public static void main(String[] args) throws IOException {
//		System.setIn(new FileInputStream("src/input.txt"));

		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine().trim());
		sb = new StringBuilder();
		
		int M = Integer.parseInt(st.nextToken()); 
		int N = Integer.parseInt(st.nextToken()); 
		Map<Integer, String> alpha = new HashMap<Integer, String>();
		alpha.put(0, "zero");
		alpha.put(1, "one");
		alpha.put(2, "two");
		alpha.put(3, "three");
		alpha.put(4, "four");
		alpha.put(5, "five");
		alpha.put(6, "six");
		alpha.put(7, "seven");
		alpha.put(8, "eight");
		alpha.put(9, "nine");
		PriorityQueue<Alpha> queue = new PriorityQueue<Alpha>();
		
		StringBuilder string;
		for (int num = M; num <= N; num++) {
			if (num < 10) {
				queue.add(new Alpha(num, alpha.get(num)));
			} else {
				string = new StringBuilder();
				string.append(alpha.get(num / 10)).append(" ").append(alpha.get(num % 10));
				queue.add(new Alpha(num, new String(string)));	
			}
		}

		while (!queue.isEmpty()) {
			System.out.println(queue.poll().num);
		}

//		System.out.println(sb);

	}
}

class Alpha implements Comparable<Alpha>{
	int num;
	String string;
	public Alpha(int num, String string) {
		this.num = num;
		this.string = string;
	}
	
	@Override
	public int compareTo(Alpha o) {
		return string.compareTo(o.string);
	}
}