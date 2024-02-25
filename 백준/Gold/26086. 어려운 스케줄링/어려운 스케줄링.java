import java.io.*;
import java.util.*;

/*
 * 

5 7 2
0 1
0 2
0 3
1
0 4
0 5
2

 */
public class Main {
	private static BufferedReader br;
	private static StringTokenizer st;
	private static StringBuilder sb;
	private static int N, Q, k, order, pid, val, totalCnt, dicCnt, index, ans;
	private static boolean dir;

	public static void main(String[] args) throws IOException {
//		System.setIn(new FileInputStream("src/input.txt"));
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine().trim());
		sb = new StringBuilder();
		N = Integer.parseInt(st.nextToken());
		Q = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		dir = true;
		ans = 0;
		Map<Integer, Integer> dic = new HashMap<Integer, Integer>();
		Deque<Integer> deque = new ArrayDeque<>();
		deque.offer(0);
		index = 0;
		val = 0;
		for (int idx = 0; idx <= N; idx++) {
			dic.put(idx, 0);
		}
		
		for (int idx = 0; idx < Q; idx++) {
			st = new StringTokenizer(br.readLine().trim());
			order = Integer.parseInt(st.nextToken());
			if (order == 0 ) {
				pid = Integer.parseInt(st.nextToken());
				totalCnt += 1;
				if (dir) {
					deque.addFirst(pid);
					index += 1;
				} else {
					deque.addLast(pid);
					index = Math.max(0, index - 1);
				}
			} else if (order == 1) {
				// poll
				while (!deque.isEmpty()) {
					val = deque.poll();
					dic.put(val, dic.get(val) + 1);
					dicCnt += 1;
				}
				deque.offer(0);
				dicCnt -= 1;
				index = 0;
				dir = true;
			} else {
				// reverse
				dir = !dir;
			}
		}
		
		// result
		// 정방향
		int cnt = 0;
//		System.out.println(deque.toString());
		int dequeCnt = deque.size();
		
		if (dir) {
			while (!deque.isEmpty() && ans == 0) {
				val = deque.pollFirst();
				if (val == 0) {
					for (int idx = 1; idx <= N; idx++) {
						if (dic.get(idx) == 0) continue;
						cnt += dic.get(idx);
						if (cnt >= k) {
							ans = idx;
							break;
						}
					}
					
				} else {
					cnt += 1;
					if (cnt == k) {
						ans = val;
						break;
					}
				}
			}
		} else {
			while (!deque.isEmpty() && ans == 0) {
				val = deque.pollLast();
				if (val == 0) {
					for (int idx = N; idx >= 1; idx--) {
						if (dic.get(idx) == 0) continue;
						cnt += dic.get(idx);
						if (cnt >= k) {
							ans = idx;
							break;
						}
					}
					
				} else {
					cnt += 1;
					if (cnt == k) {
						ans = val;
						break;
					}
				}
			}
		}
		
//		if (dir) {
//			// 해당 값이 dic 안에 있을 경우
//			if (k >= index + 1 && k <= index + dicCnt) {
//				cnt = index;
//				for (int idx = 1; idx <= N; idx++) {
//					val = dic.get(idx);
//					if (val == 0) continue;
//					cnt += val;
//					if (k <= cnt) {
//						ans = idx;
//						break;
//					}
//				}
//			} else {
//				// 그냥 하나씩 다 뽑자..
//				while (!deque.isEmpty()) {
//					val = deque.pollFirst();
//					if (val == 0) {
//						cnt += dicCnt;
//					} else {
//						cnt += 1;
//					}
//					if (cnt == k) {
//						ans = val;
//						break;
//					}
//				}
//			}
//		} else {
////			System.out.println(index);
////			System.out.println(deque.size());
//			index = deque.size() - 1 - index;
////			System.out.println(index);
//			if (k >= index + 1 && k <= index + dicCnt) {
//				cnt = index;
//				for (int idx = N; idx >= 1; idx--) {
//					val = dic.get(idx);
//					if (val == 0) continue;
//					cnt += val;
//					if (k <= cnt) {
//						ans = idx;
//						break;
//					}
//				}
//			} else {
////				 그냥 하나씩 다 뽑자..
////				System.out.println("5555");
////				System.out.println(deque.toString());
//				while (!deque.isEmpty()) {
//					val = deque.pollLast();
//					if (val == 0) {
//						cnt += dicCnt;
//					} else {
//						cnt += 1;
//					}
//					if (cnt == k) {
//						ans = val;
//						break;
//					}
//				}
//			}	
//		}
//		System.out.println(deque.toString());
		System.out.println(ans);

	}

}
