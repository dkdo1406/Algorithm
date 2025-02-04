import java.util.*;
import java.io.*;

/**
 * BOJ_1697_숨바꼭질_김형중
 * 
 * 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
 * 	
 * 접근 방법
 * 수빈이는 +1, -1, 2*X 위치로 이동한다.
 * 
 * @author SSAFY
 *
 */
public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static StringBuilder sb;
	
	static int N, K, ans[];

	public static void main(String[] args) throws IOException {
//		System.setIn(new FileInputStream("src/input.txt"));
		
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine().trim());
		sb = new StringBuilder();

		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		ans = new int[300000];
		
		for (int idx = 0; idx < 300000; idx++) {
			ans[idx] = 500000;
		}
		// 현재 위치는 0으로 초기화한다.
		ans[N] = 0;	
		for (int idx = N; idx >= 0; idx--) {
			ans[idx] = Math.min(ans[idx], ans[idx + 1] + 1);
			ans[idx * 2] = Math.min(ans[idx * 2], ans[idx] + 1);
		}
		
		for (int idx = N + 1; idx < 100001; idx++) {
			if (idx % 2 == 0) {
				ans[idx] = Math.min(ans[idx], ans[idx / 2] + 1);
			}
			ans[idx] = Math.min(ans[idx], ans[idx - 1] + 1);
			ans[idx] = Math.min(ans[idx], ans[idx + 1] + 1);
			ans[idx * 2] = Math.min(ans[idx * 2], ans[idx] + 1);
		}



		System.out.println(ans[K]);

	}

}