import java.util.*;
import java.io.*;
import java.math.BigInteger;

/*
 * 스위치 켜고 끄기 1244
 * 
 * 남자는 자신이 받은 숫자의 배수 스위치를 작동
 * 여자는 자신이 받은 숫자를 중심으로 좌, 우가 같은 것들을 비교하여 교체
 * 
 */
public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static StringBuilder sb;
	public static void main(String[] args) throws IOException {
//		System.setIn(new FileInputStream("src/input.txt")); 

		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine().trim(), " ");
		
		int N = Integer.parseInt(st.nextToken());
		int[] arr = new int[N];
		st = new StringTokenizer(br.readLine().trim(), " ");
		for (int idx = 0; idx < N; idx++) {
			arr[idx] = Integer.parseInt(st.nextToken());
		}
		int person = Integer.parseInt(br.readLine().trim());
		for (int idx = 0; idx < person; idx++) {
			st = new StringTokenizer(br.readLine().trim(), " ");
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			if (n == 1) {
				for (int manIdx = m - 1; manIdx < N; manIdx += m) {
					arr[manIdx] = 1 - arr[manIdx];
				}
			} else {
				int left = m - 2;
				int right = m;
				arr[m - 1] = 1 - arr[m - 1];
				while (left >= 0 && right < N && arr[left] == arr[right]) {
					arr[left] = 1 - arr[left];
					arr[right] = 1 - arr[right];
					left -= 1;
					right += 1;
				}
			}
		}
		sb = new StringBuilder();
		for (int idx = 1; idx < N + 1; idx++) {
			sb.append(arr[idx - 1] + " ");
			if (idx % 20 == 0) {
				sb.append("\n");
			}
		}
		
		System.out.println(sb);

	}

}
