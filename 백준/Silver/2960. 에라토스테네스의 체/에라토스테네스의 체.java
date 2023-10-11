import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static StringBuilder sb;
	
	static int a, b;
	public static void main(String args[]) throws Exception {
//		System.setIn(new FileInputStream("src/input.txt"));

		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine().trim());
		sb = new StringBuilder();
		
		a = Integer.parseInt(st.nextToken());
		b = Integer.parseInt(st.nextToken());
		
		boolean[] numberList = new boolean[a + 1];
		
		for (int prime = 2; prime <= a; prime++) {
			if (b == 0) break;
			if (numberList[prime] == false) {
				for (int cnt = 1; cnt <= a / prime; cnt++) {
					if (numberList[prime * cnt] == false) {
						numberList[prime * cnt] = true;
						b -= 1;
						if (b == 0) {
							sb.append(prime * cnt);
						}
					}
				}
			}
		}

		System.out.println(sb);
	}
}
