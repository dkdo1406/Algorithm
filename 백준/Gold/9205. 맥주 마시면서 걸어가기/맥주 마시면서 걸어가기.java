import java.io.*;
import java.util.*;


/**
 * BOJ_9205_맥주마시면서걸어가기_김형중
 * 
 * 시작 한박스(20병), 50미터에 한병 마신다.
 * 편의점에 방문하면 다 마신병과 교환가능
 * 맥주의 총 용량 : 50 * 20 => 1000
 *  
 * 접근 방법
 * 모든 지점간 거리를 세팅한다. 계산은 abs(x1 - x2) + abs(y1 - y2)
 * 만약 거리가 1000이 넘는다면 1001로 고정한다.
 * 거리가 1000보다 작거나 같다면 계산 결고에서 % 50을 해준다.
 * 세팅이 끝나면 플로이드 워샬을 사용하여 모든 위치를 계산해준다.
 * 마지막으로 결과값에 graph[0][N+1]를 넣어준다.
 * 
 * 
 * 
 * @author SSAFY
 *
 */
public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static StringBuilder sb;

	static int N, pos[][], graph[][], store[][], festival[];
	static String ans;


	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("src/input.txt"));
		br = new BufferedReader(new InputStreamReader(System.in));

		sb = new StringBuilder();
		st = new StringTokenizer(br.readLine().trim());
		int T = Integer.parseInt(st.nextToken());
		int r, c;
		for (int tc = 1; tc <= T; tc++) {
			N = Integer.parseInt(br.readLine().trim());
			graph = new int[N + 2][N + 2];
			ans = "happy";
			pos = new int[N + 2][2];
			store = new int[N][2];
			st = new StringTokenizer(br.readLine().trim());
			c = Integer.parseInt(st.nextToken());
			r = Integer.parseInt(st.nextToken());
			pos[0][0] = r;
			pos[0][1] = c;
			
			// 가게 위치
			for (int idx = 1; idx < N + 1; idx++) {
				st = new StringTokenizer(br.readLine().trim());
				c = Integer.parseInt(st.nextToken());
				r = Integer.parseInt(st.nextToken());
				pos[idx][0] = r;
				pos[idx][1] = c;
			}

			// 목적지
			st = new StringTokenizer(br.readLine().trim());
			c = Integer.parseInt(st.nextToken());
			r = Integer.parseInt(st.nextToken());
			pos[N+1][0] = r;
			pos[N+1][1] = c;
			
			
			// 0 : 출발지점, N + 1 도착지점

			
			// 초기화 및 모든 지점의 거리 계산
			for (int start = 0; start < N + 2; start++) {
				for (int end = 0; end < N + 2; end++) {
					if (start != end) {
						int distince = Math.abs(pos[start][0] - pos[end][0]) + Math.abs(pos[start][1] - pos[end][1]);
						graph[start][end] = Math.min(1001, distince);
						// 각 지점에 도착할 수 있다면 맥주 교체를 할 수 있다.
						if (graph[start][end] <= 1000) {
							graph[start][end] %= 50;
						}
					}
					
				}
			}
			
			
			// 플로이드 워샬
			for (int transit = 0; transit < N + 2; transit++) {
				for (int start = 0; start < N + 2; start++) {
					if (start == transit) continue;
					for (int end = 0; end < N + 2; end++) {
						// 출발지와 도착지가 같으면 pass
						if (start == end || end == transit) continue;
						
						// 출발지 - 경유지 + 경유지 - 도착지
						int distince = graph[start][transit] + graph[transit][end];
						
						// 기존 경로와 경유지를 거친 경로 중 작은 값을 적용
						graph[start][end] = Math.min(graph[start][end], distince);
						
						// 각 지점에 도착할 수 있다면 맥주 교체를 할 수 있다.
						if (graph[start][end] <= 1000) {
							graph[start][end] %= 50;
						}
					}
				}
			}
			
			if (graph[0][N+1] <= 1000) {
				ans = "happy";
			} else {
				ans = "sad";
			}
			
			sb.append(ans).append("\n");
		}
		
		System.out.println(sb);
	}

}