import java.io.*;
import java.util.*;


/**
 * BOJ_1912_연속합_김형중
 *  
 * 문제
 * n개의 정수로이루어진 임의의 수열
 * 몇개를 선택하여 구할 수 있는 합 중 가증 큰값 수는 1개 이상 선택
 * 
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
		
		st = new StringTokenizer(br.readLine().trim());
		int[] dp = new int[N];
		for (int idx = 0; idx < N; idx++) {
			dp[idx] = Integer.parseInt(st.nextToken());
			
		}
		int ans = dp[0];
		for (int idx = 1; idx < N; idx++) {
			dp[idx] = Math.max(dp[idx], dp[idx - 1] + dp[idx]);
			ans = Math.max(ans, dp[idx]);
		}
		
		
		System.out.println(ans);

	}

}