import java.io.*;
import java.math.BigInteger;
import java.util.*;

/**
 * boj17069 파이프옮기기2
 * 
 * →, ↘, ↓ 방향으로 옮길 수 있다.
 * 회전은 45도만 가능
 * 
 * 벽 긁기 불가능
 * 처음 위치는 (1,1)과 (1,2)를 차지
 * (N, N)로 이동가능한 방법의 개수를 구하자
 */
public class Main {
	private static BufferedReader br;
	private static StringTokenizer st;
	private static StringBuilder sb;
	private static int N, graph[][];
	private static BigInteger ansGraph[][][], ans;

	public static void main(String[] args) throws IOException {
//		System.setIn(new FileInputStream("src/input.txt"));
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine().trim());
		sb = new StringBuilder();
		N = Integer.parseInt(st.nextToken());
		
		graph = new int[N][N];
		// 0 : 가로 1 : 대각선 2 : 세로
		ansGraph = new BigInteger[N][N][3];
		
		for (int r = 0; r < N; r++) {
			st = new StringTokenizer(br.readLine().trim());
			for (int c = 0; c < N; c++) {
				graph[r][c] = Integer.parseInt(st.nextToken());
				ansGraph[r][c][0] = new BigInteger("0");
				ansGraph[r][c][1] = new BigInteger("0");
				ansGraph[r][c][2] = new BigInteger("0");
			}
		}
		
		// 초기세팅
		if (graph[0][2] == 0) {
			ansGraph[0][2][0] = ansGraph[0][2][0].add(new BigInteger("1"));
			if (graph[1][2] == 0 && graph[1][1] == 0) {
				ansGraph[1][2][1] = ansGraph[1][2][1].add(new BigInteger("1"));
				if (graph[2][2] == 0) {
					ansGraph[2][2][2] = ansGraph[2][2][2].add(ansGraph[1][2][1]);
					for (int r = 3; r < N; r++) {
						if (graph[r][2] != 0) break;
						ansGraph[r][2][2] = ansGraph[r][2][2].add(ansGraph[r-1][2][2]);
					}
				}
				
			}
		}
		// 가로 
		for (int c = 3; c < N; c++) {
			if (graph[0][c] != 0) break;
			ansGraph[0][c][0] = ansGraph[0][c][0].add(ansGraph[0][c-1][0]);
		}
		
		
		for (int r = 1; r < N; r++) {
			for (int c = 3; c < N; c++) {
				// 가로
				if (graph[r][c] == 0) {
					// 가로방향
					ansGraph[r][c][0] = ansGraph[r][c][0].add(ansGraph[r][c-1][0]); // 가로
					ansGraph[r][c][0] = ansGraph[r][c][0].add(ansGraph[r][c-1][1]); // 대각선
					// 세로방향
					ansGraph[r][c][2] = ansGraph[r][c][2].add(ansGraph[r-1][c][2]); // 세로
					ansGraph[r][c][2] = ansGraph[r][c][2].add(ansGraph[r-1][c][1]); // 대각선
					// 대각으로 오려면 왼쪽과 위가 0이면 안된다.
					if (graph[r-1][c] == 0 && graph[r][c-1] == 0) {
						ansGraph[r][c][1] = ansGraph[r][c][1].add(ansGraph[r-1][c-1][1]); // 대각선
						ansGraph[r][c][1] = ansGraph[r][c][1].add(ansGraph[r-1][c-1][0]); // 가로
						ansGraph[r][c][1] = ansGraph[r][c][1].add(ansGraph[r-1][c-1][2]); // 세로
					}
				}
			}
		}
		ans = ansGraph[N-1][N-1][0].add(ansGraph[N-1][N-1][1]).add(ansGraph[N-1][N-1][2]);
		System.out.println(ans);

	}

}
