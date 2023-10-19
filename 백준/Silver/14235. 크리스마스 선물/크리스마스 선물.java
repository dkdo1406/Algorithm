import java.io.*;
import java.util.*;

/**
 * BOJ_14235_크리스마스선물_김형중
 *
 * 문제
 * 산타가 착한 아이를 만날 때마다 자신이 가진 선물 중 가장 가치가 큰 물건을 준다.
 *
 * 접근 방법
 * 우선수위 큐를 사용하여 가치가 가장 큰 선물을 맨 앞으로 나오게 한다.
 */
public class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static StringBuilder sb;

    static int n, num, present;
    public static void main(String[] args) throws IOException {
//        System.setIn(new FileInputStream("src/input.txt"));
        br = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuilder();
        // 총 입력 수
        n = Integer.parseInt(br.readLine().trim());

        Queue<Integer> queue = new PriorityQueue<>();

        for (int idx = 0; idx < n; idx++) {
            st = new StringTokenizer(br.readLine().trim());
            // 첫번째 입력값이 0이면 착한 아이, 0이 아니면 입력 받을 선물
            num = Integer.parseInt(st.nextToken());
            if (num == 0) {
                if (queue.isEmpty()) {
                    sb.append(-1).append("\n");
                } else {
                    sb.append(-queue.poll()).append("\n");
                }
            } else {
                for (int cycle = 0; cycle < num; cycle++) {
                    present = Integer.parseInt(st.nextToken());
                    queue.offer(-present);
                }
            }
        }
        System.out.println(sb);
    }
}