import java.util.*;
import java.io.*;
import java.math.BigInteger;

public class Main {

	public static void main(String[] args) throws IOException {
//		System.setIn(new FileInputStream("src/input.txt")); 

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int time;
		BigInteger[] dp = new BigInteger[491];
		dp[0] = new BigInteger("0");
		dp[1] = new BigInteger("1");
		dp[2] = new BigInteger("1");
		for (int idx = 3; idx < 491; idx++) {
			dp[idx] = dp[idx - 2].add(dp[idx - 1]);
		}
		while (true) {
			StringTokenizer st = new StringTokenizer(br.readLine().trim(), " ");
			time = Integer.parseInt(st.nextToken());
			if (time == -1) break;
			System.out.println("Hour " + time + ": " + dp[time] + " cow(s) affected");
			
		}
		
	}
}
