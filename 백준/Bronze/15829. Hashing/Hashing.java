import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br;
    private static StringTokenizer st;
    private static StringBuilder sb;
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine().trim());
        sb = new StringBuilder();
        
        int N =  Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine().trim());
        String S = st.nextToken();
        // int r = 31;
        double M = 1234567891;
        double ans = 0;
        int[] r = new int[] {1, 31, 31*31, 31*31*31, 31*31*31*31};
        
        for (int idx = 0; idx < N; idx++) {
            ans += (S.charAt(idx)-96) * r[idx];
        }
        System.out.println((int)(ans % M));
        


    }
}
