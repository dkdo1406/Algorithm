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

	static BigInteger s1, s2, s3;
	public static void main(String[] args) throws IOException {
//		System.setIn(new FileInputStream("src/input.txt"));

		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine().trim(), " ");
		sb = new StringBuilder();
		
		
		long N = Long.parseLong(st.nextToken()); // 피보나치 

		s1 = new BigInteger("0");
		s2 = new BigInteger("1");
		
		if (N == 0) {
			s3 = new BigInteger("0");
		}
		
		for(int idx = 2; idx < N + 2; idx++) {
			s3 = new BigInteger("0").add(s1).add(s2).divideAndRemainder(new BigInteger("1000000007"))[1];
			s2 = new BigInteger("0").add(s1);
			s1 = new BigInteger("0").add(s3);
			
		}

//		sb.append(dp[(int)N]);
		sb.append(s3);
		System.out.println(sb);

	}
}
