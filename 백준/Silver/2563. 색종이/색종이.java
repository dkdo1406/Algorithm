import java.io.*;
import java.util.*;

/*
 * BOJ_2563_색종이_김형중
 * 
 * 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.
 * 
 * 
 * 접근방법
 * 도화지의 크기는 100 * 100이다.
 * 이를 2차원 배열로 만들고 모두 0으로 채운다.
 * 색종이의 x와 y좌표가 주어지는데 색종이의 크기가 10으로 고정되어 있어
 * 색종이의 좌표 (x, y) ~ (x + 9, y + 9) 까지 1로 채워준다.
 * 모든 색종이의 좌표를 받고 1로 채워준 후 도화지에서 1의 개수를 출력한다.
 * 
 */

public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static StringBuilder sb;
	
	public static void main(String args[]) throws Exception {
//		System.setIn(new FileInputStream("src/input.txt")); 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		sb = new StringBuilder();


		int N = Integer.parseInt(st.nextToken().trim());

		int[][] graph = new int[100][100];
		
		for (int idx = 0; idx < N; idx++) {
			st = new StringTokenizer(br.readLine().trim());
			int X = Integer.parseInt(st.nextToken().trim()) - 1;
			int Y = Integer.parseInt(st.nextToken().trim()) - 1;
			
			for (int r = Y; r < Y + 10; r++) {
				for (int c = X; c < X + 10; c++) {
					graph[r][c] = 1;
				}
			}
		}
		int ans = 0;
		for (int r = 0; r < 100; r++) {
			for (int c = 0; c < 100; c++) {
				ans += graph[r][c];
			}
		}
		sb.append(ans);
		
		// 출력
		System.out.println(sb);
	}
}