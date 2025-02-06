import java.util.*;
import java.io.*;

public class Main {
    private static BufferedReader br;
    private static StringTokenizer st;
    private static StringBuilder sb;
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine().trim());
        sb = new StringBuilder();
        int val = 0;
        String order;
        LinkedList<Integer> list = new LinkedList<>();
        int N = Integer.parseInt(st.nextToken());
        for (int idx = 0; idx < N; idx++) {
            st = new StringTokenizer(br.readLine().trim());
            order = st.nextToken();

            switch (order) {
                case "push":
                    val = Integer.parseInt(st.nextToken());
                    list.add(val);
                    break;
                case "pop":
                    if (list.isEmpty()) {
                        sb.append(-1);
                    } else {
                        sb.append(list.removeFirst());
                    }
                    sb.append("\n");
                    break;
                
                case "size":
                    sb.append(list.size());
                    sb.append("\n");
                    break;
                case "empty":
                    if (list.isEmpty()) {
                        sb.append(1);
                    } else {
                        sb.append(0);
                    }
                    sb.append("\n");
                    break;
                case "front":
                    if (list.isEmpty()) {
                        sb.append(-1);
                    } else {
                        sb.append(list.getFirst());
                    }
                    sb.append("\n");
                    break;
                case "back":
                if (list.isEmpty()) {
                    sb.append(-1);
                } else {
                    sb.append(list.getLast());
                }
                sb.append("\n");
                    break;
                default:
                    break;
            }
            
        }
        System.out.println(sb);
    }
}
