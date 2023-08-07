import java.util.*;
import java.io.*;
import java.math.BigInteger;

/*
 * BOJ_10826_피보나치수4_김형중
 *
 * n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
 * 
 * 구현
 * N을 입력 받는다.
 * 주어진 N + 1 만큼 배열을 생성한다.
 * 그리고 초기값으로 0번 인덱스에 0을, 1번 인덱스에 1을 저장한다.
 * idx 2부터 시작하여 N까지 idx = idx - 1 + idx - 2를 하여 저장한다.
 * 결과값으로 dp[N]를 출력한다.
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
		
		N = Integer.parseInt(st.nextToken()); // 피보나치 
		BigInteger[] dp;
		if (N < 1) {
			dp = new BigInteger[2];
		} else {
			dp = new BigInteger[N + 1];
		}
		dp[0] = new BigInteger("0");
		dp[1] = new BigInteger("1");

		for(int idx = 2; idx < N + 1; idx++) {
			dp[idx] = dp[idx - 1].add(dp[idx - 2]);
		}

		sb.append(dp[N]);
		System.out.println(sb);

	}
}
