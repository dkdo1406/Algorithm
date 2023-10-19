import java.util.*;
import java.io.*;

/**
 * SWEA_4013_특이한자석_김형중
 * 
 * 문제
 * 자석이 달린 4개의 판, 각 판은 8개날을 가지며 자성이 있음
 * 날 마다 N극 또는 S극의 자성을 띔
 * 빨간색 화살표 위치에 날 하나가 오도록 배치
 * 임의의 자석을 한칸씩 k번 회전시키면 1칸회전할때마다 붙어있는 자석은 날의 자성이 다를 경우에
 * 반대 방향으로 1칸 회전
 * 무작위 회전 후 빨간색 화살표 위치마다 점수 배점
 * 1번 : S극 1점
 * 2번 : S극 2점
 * 3번 : S극 4점
 * 4번 : S극 8점
 * 
 * 
 * 
 * 접근 방법
 * 관계를 나타내는데 Disjoint Set Union을 사용하여
 * 몇개의 무리가 있는지 찾는다.
 * 
 * @author SSAFY
 *
 */

class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static StringBuilder sb;


	public static void main(String args[]) throws Exception {
		//		System.setIn(new FileInputStream("src/s_input.txt"));
		br = new BufferedReader(new InputStreamReader(System.in));
		sb = new StringBuilder();

		int N, M, ans, K, arr[][], num, dir, left, right;
		arr = new int[4][8];

		List<Integer>[] q = new ArrayList[4];



		ans = 0;


		for (int idx = 0; idx < 4; idx++) {
			String S = br.readLine().trim();
//			st = new StringTokenizer(br.readLine().trim());
			q[idx] = new ArrayList<Integer>();
			for (int index = 0; index < 8; index++) {
				q[idx].add(S.charAt(index) - '0');
			}
		}

		K = Integer.parseInt(br.readLine().trim());
		for (int idx = 0; idx < K; idx++) {
			st = new StringTokenizer(br.readLine().trim());
			num = Integer.parseInt(st.nextToken()) - 1; // 자석번호
			dir = Integer.parseInt(st.nextToken()); // 방향
			// 1 : 시계방향, -1 : 반시계방향
			int[] spin = new int[4];
			spin[num] = dir;
			// 2 와 6을 계속 비교

			Queue<Integer> queue = new ArrayDeque<Integer>();
			queue.offer(num);
			while (!queue.isEmpty()) {
				num = queue.poll();
				left = num - 1;
				right = num + 1;
				if (left >= 0 && spin[left] == 0) {
					if (q[num].get(6) != q[left].get(2)) {
						// left도 회전 가능
						spin[left] = spin[num] * -1;
						queue.offer(left);
					}
				}
				if (right < 4 && spin[right] == 0) {
					if (q[num].get(2) != q[right].get(6)) {
						// right도 회전 가능
						spin[right] = spin[num] * -1;
						queue.offer(right);
					}
				}	
			}

			for (int index = 0; index < 4; index++) {
				if (spin[index] == -1) {
					q[index].add(q[index].remove(0));
				} else if (spin[index] == 1) {
					q[index].add(0, q[index].remove(7));
				}
			}

		}

		for (int idx = 0; idx < 4; idx++) {
			if (q[idx].get(0) == 1) {
				ans += Math.pow(2, idx);
			}
		}

		System.out.println(ans);

	}
}