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
        
        int A = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine().trim());
        int B = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine().trim());
        int C = Integer.parseInt(st.nextToken());
        System.out.println(A + B - C);
        sb.append(String.valueOf(A));
        sb.append(String.valueOf(B));
        System.out.println(Integer.parseInt(sb.toString()) - C);
    }
}
