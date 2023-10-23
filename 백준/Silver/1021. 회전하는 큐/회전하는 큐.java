import java.io.*;
import java.util.*;


/**
 * BOJ_1021_회전하는_김형중
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
	static List<Integer> list;

	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("src/s_input.txt"));
		br = new BufferedReader(new InputStreamReader(System.in));

		sb = new StringBuilder();
		st = new StringTokenizer(br.readLine().trim());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		list = new ArrayList<Integer>();
		for (int idx = 1; idx <= N; idx++) {
			list.add(idx);
		}
		int pointer = 0;
		st = new StringTokenizer(br.readLine().trim());
		int ans = 0;
		for (int idx = 0; idx < M; idx++) {
			int num = Integer.parseInt(st.nextToken());
			if (list.get(pointer) != num) {
				int index = bianrySearch(num);
				// 현재 pointer를 앞과 뒤 중 갈 거리를 선택한다.
				// 왼쪽으로 계속 이동시켜 해당 위치에 도착
				int dist = list.size();
//				System.out.println(pointer + " " + index);
				if (pointer < index) {
					dist = Math.min(pointer + dist - index, index - pointer);
				} else {
					dist = Math.min(index + dist - pointer, pointer - index);
				}
				ans += dist;
				pointer = index;
				
			}
			list.remove(pointer);
			
			if (list.size() - 1 < pointer) {
				pointer = 0;
			}
			
			

//			System.out.println(ans);
//			System.out.println(pointer + " " + list);
		}
		
		System.out.println(ans);
		
		
		
		
		
	}
	
	private static int bianrySearch(int n) {
		int l = 0;
		int r = list.size();
		int c = 0;
		while (l <= r) {
			c = (l + r) / 2;
			if (list.get(c) == n) {
				return c;
			}
			if (list.get(c) < n) {
				l = c + 1;
			} else {
				r = c - 1;
			}
		}
		return c;
		
	}

}